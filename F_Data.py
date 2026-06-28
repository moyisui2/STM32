import re
import STM32H7
from STM32H7 import (
    ALL_STM32H7_DATA, ALL_STM32H7_DATA_H, WW_DATA,
    DEFINE_DATA, DEFINE_DATA_DefineX, WAISHE_DATA
)
ALL_STM32H7_NAMES = list(ALL_STM32H7_DATA_H.keys())
file_path = "stm32f103c8t6_@V4.0.txt"
try:
    with open(file_path, encoding="utf-8") as DU:
        read = DU.read()
except FileNotFoundError:
    print("文件未找到！")
    exit()



DATA = ""
DATA0 = ""
DATA1 = ""
DATA2 = ""

def TMode1_STM32F103C8T6(hanshu):
    global DATA
    DATA = ""
    HanShu = hanshu
    UI = r"—{10,}\s函数名：" + HanShu + r"\s函数原型.*?—{10,}"
    Data = re.findall(UI, read, re.DOTALL)
    if not Data:
        DATA += f"与【{HanShu}】有关的函数未找到！\n"
    if Data:
        DATA += f"【{HanShu}相关函数信息】\n"
        DATA += "\n".join(Data) + "\n\n\n"
        for i in Data:
            un = re.findall(r"输入参数[0-9]+：([^：]+)：", i, re.DOTALL)
            if un:
                for param in un:
                    DATA += f"【{HanShu}函数参数】\n\n"
                    InitTypeDef = re.findall("InitStruct", param, re.DOTALL)
                    asj = re.findall(r"—{5,}\s*" + re.escape(param) + r".*?—{5,}", read, re.DOTALL)
                    if not InitTypeDef:
                        if not asj:
                            DATA += f"\n未找到参数【{param}】的详细信息！\n"
                        else:
                            for l in asj:
                                DATA += l
                    else:
                        CCAD = re.findall(r"([^：]+)_", param, re.DOTALL)
                        for m in CCAD:
                            CHi = re.findall(r"—{5,}\s*" + m + r"_InitTypeDef.*?#{5,}", read, re.DOTALL)
                            xxy = re.findall(m + r"_(.*?)InitStruct", param, re.DOTALL)
                            if xxy:
                                if "" not in xxy:
                                    for x in xxy:
                                        CHi1 = re.findall(r"—{5,}\s*" + m + r"_" + x + r"InitTypeDef.*?#{5,}", read, re.DOTALL)
                                        if CHi1:
                                            for n in CHi1:
                                                DATA += n
                                        else:
                                            DATA += f"\n未找到参数【{param}】的详细信息！\n"
                            if CHi:
                                for n in CHi:
                                    DATA += n
                            if not CHi and not xxy:
                                DATA += f"\n未找到参数【{param}】的详细信息！\n"
    return DATA

def TMode1_STM32H7(hanshu):
    global DATA
    DATA = ""
    GFH = "__" + f"{hanshu}"
    if hanshu in ALL_STM32H7_NAMES:
        DATA += f"【{hanshu}】相关信息如下：\n\n"
        info = ALL_STM32H7_DATA[hanshu]
        for key in ["函数原名","函数描述","参数1","参数2","参数3","参数4","参数5",
                     "函数参数1详细取值","函数参数2详细取值","函数参数3详细取值",
                     "函数参数4详细取值","函数参数5详细取值","返回值","函数用法","注意事项"]:
            if key in info:
                DATA += f"【{key}】：{info[key]}\n"
    elif hanshu in WAISHE_DATA:
        DATA += f"\n【{hanshu}】相关信息如下：\n\n"
        OOO = f"{hanshu}_X"
        DATA += f"【简要介绍】  {WAISHE_DATA[hanshu]}\n\n"
        DATA += f"【详细介绍】  {WAISHE_DATA[OOO]}\n\n"
    elif hanshu in DEFINE_DATA:
        DATA += f"\n【{hanshu}】相关信息如下：\n\n"
        DATA += f"{DEFINE_DATA[hanshu]}\n\n"
    elif GFH in DEFINE_DATA:
        DATA += f"\n【{hanshu}】相关信息如下：\n\n"
        DATA += f"{DEFINE_DATA[GFH]}\n\n"
    elif hanshu in DEFINE_DATA_DefineX:
        DATA += f"\n【{hanshu}】相关信息如下：\n\n"
        DATA += f"{DEFINE_DATA_DefineX[hanshu]}\n\n"
    else:
        DATA += f"与【{hanshu}】有关的信息未找到！\n"
    return DATA

def TMode2_STM32F103C8T6(data):
    global DATA0
    DATA0 = ""
    if data == "全部":
        XData = re.findall(r"#{10,}\s!—{5,}\sADC.*?#{10,}", read, re.DOTALL)
        DATA0 = XData[0] if XData else ""
    else:
        XData = re.findall(r"!—{5,}\s" + data + r".*?!—{5,}", read, re.DOTALL)
        DATA0 = XData[0] if XData else ""
    return DATA0

def TMode2_STM32H7(data):
    global DATA0
    DATA0 = ""
    if data == "全部":
        count = len(ALL_STM32H7_NAMES)
        DATA0 += f"【共有{count}个相关函数】\n\n"
        DATA0 += "\n".join(ALL_STM32H7_NAMES) + "\n"
    else:
        DATA0 += f"【{data}相关函数信息】\n"
        funcs = WW_DATA.get(data, [])
        DATA0 += f"【共有{len(funcs)}个相关函数】\n\n"
        for f in funcs:
            DATA0 += f"【{f}】:{ALL_STM32H7_DATA[f]['函数描述']}\n\n"
        return DATA0

def TMode3_STM32F103C8T6(data):
    global DATA1
    DATA1 = ""
    YN = data
    YNData = re.findall(r"—{5,}！！！\s" + YN + r".*?—{5,}！！！", read, re.DOTALL)
    if not YNData:
        return
    text = YNData[0]
    steps = re.split(r"—{5,}\d\s", text)
    if len(steps) > 1:
        intro = steps[0]
        DATA1 += f"【{YN}介绍】\n{intro}\n"
        for i, step in enumerate(steps[1:], start=1):
            parts = re.split(r"!##\s", step, maxsplit=1)
            if len(parts) == 2:
                DATA1 += f"\n【相关函数信息】\n{parts[0]}\n"
                DATA1 += f"\n【相关注意事项】\n{parts[1]}\n"
            else:
                DATA1 += f"\n【步骤{i}】\n{step}\n"
    return DATA1


def TMode3_STM32H7(data):
    global DATA1
    DATA1 = ""
    if data == "请选择":
        DATA1 += f"【请选择】\n\n"
    else:
        DATA1 += f"【简要介绍】  {WAISHE_DATA[data]}\n\n"
        DATA1 += f"【详细介绍】  {WAISHE_DATA[data + '_X']}\n"
    return DATA1

def TMode3_STM32H7X(data, base):
    global DATA1
    DATA1 = ""
    if data == "请选择":
        DATA1 += f"【请选择】\n\n"
    else:
        DATA1 += f"【{data}】\n\n{WAISHE_DATA[base][data]}"
    return DATA1

def TMode4_STM32F103C8T6(data):
    global DATA2
    DATA2 = ""
    if data == "I2C介绍和软件I2C的编写":
        I2CData = re.findall(r"—{5,}I2C.*?—{5,}I2C", read, re.DOTALL)
        DATA2 = "【I2C通信协议详解及STM32F103C8T6软件模拟实现】\n" + "\n".join(I2CData)
    elif data == "中断服务函数的介绍和使用":
        ZHONGDUANData = re.findall(r"—{5,}Zhon#.*?—{5,}Zhon#", read, re.DOTALL)
        DATA2 = "【中断函数介绍和使用】\n" + "\n".join(ZHONGDUANData)
    elif data == "中断服务函数列表":
        resetData = re.findall(r"—{5,}ZhonXXend.*?—{5,}ZhonXXend", read, re.DOTALL)
        DATA2 = "【中断服务函数列表】\n" + "\n".join(resetData)
    elif data == "__WFI()和__WFE()的使用":
        WFIData = re.findall(r"—{5,}WFI.*?—{5,}WFI", read, re.DOTALL)
        DATA2 = "【__WFI()和__WFE()的使用】\n" + "\n".join(WFIData)
    return DATA2