import re
file_path = "stm32f103c8t6_@.txt"
print(f"\033[92m**************************欢迎使用STM32查询系统1.0*****************************\033[0m")
print(f"\033[91m***********************本程序由广西科技大学  @一岁  编写*************************\033[0m")
print(f"\033[92m注：本程序仅支持STM32F103C8T6相关函数的查询\033[0m")
def main():
    #模式选择：
    print("\n\033[34m ——————————————————————————————————————————\033[0m",end="")
    print("\n\033[34m请选择查询模式：\033[0m")
    print("[1] 输入函数名查找函数")
    print("[2] 查看函数名")
    print("[3] 查询STM32F103C8T6的引脚定义",end="")
    print("\n\033[34m ——————————————————————————————————————————\033[0m")
    Mode=input()
    if Mode=="1":
        Mode1()
    if Mode=="2":
        Mode2()
    if Mode=="3":
        Mode3()
    if Mode not in ["1","2","3"]:
        print("\033[91m输入错误，请重新选择模式！\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()

#模式1
def Mode1():
    #函数查找：
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"\n\033[91m❌ 错误：未找到文件「{file_path}」！\033[0m")
        print("\033[91m请检查文件是否存在，或文件路径是否正确。\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()
    DU=open(file_path,encoding="utf-8")
    read=DU.read()
    print("\033[34m请输入要查找的函数名：\033[0m")
    HanShu=input()
    if HanShu.strip()=="":
        print("\033[91m输入不能为空，请重新输入！\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()
    UI=r"—{10,}\s函数名："+HanShu+r".*?—{10,}"
    Data=re.findall(UI,read,re.DOTALL)
    if not Data:
        print(f"\033[91m未找到函数{HanShu}，请检查输入是否正确！\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()
    if Data:
        CI=[]
        print(f"\n\n\033[92m{HanShu}函数查找结果如下\033[0m")
        for i in Data:
            print(i)
        for i in Data:
            un=re.findall(r"输入参数[0-9]+：([^：]+)：",i,re.DOTALL)
            #如果有参数
            if un:
                CI.append(un)
                for j in CI:
                    print("\033[92m参数查询如下：\033[0m")
                    for k in j:
                        InitTypeDef=re.findall("InitStruct",k,re.DOTALL)
                        asj = re.findall(r"—{5,}\s*"+re.escape(k)+r".*?—{5,}",read, re.DOTALL)
                        if not InitTypeDef:
                            if not asj:
                                print(f"\033[91m未找到参数{k}的详细信息！\033[0m")
                            if asj:
                                for l in asj:
                                    print(l)
                        if InitTypeDef:
                            CCAD=re.findall(r"([^：]+)_",k,re.DOTALL)
                            for m in CCAD:
                                CHi=re.findall(r"—{5,}\s*"+m+r"_InitTypeDef.*?#{5,}",read,re.DOTALL)
                                if not CHi:
                                    print(f"\033[91m未找到参数{k}的详细信息！\033[0m")
                                if CHi:
                                    for n in CHi:
                                        print(n)
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()

#模式2
def Mode2():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"\n\033[91m❌ 错误：未找到文件「{file_path}」！\033[0m")
        print("\033[91m请检查文件是否存在，或文件路径是否正确。\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()
    XData=re.findall(r"#{10,}\s!—{5,}\sADC.*?#{10,}",read,re.DOTALL)
    print(f"\n\n\033[92m函数列表如下：\033[0m")
    for i in XData:
        print(i)
    print(f"\n\033[92m是否要单独查看某个外设的函数列表？(Y/N)\033[0m")
    YN=input()
    if YN in ["Y"]:
        print("\n\n\033[92m请输入要查看的外设名称：\033[0m")
        print("可输入：ADC、GPIO、USART等外设名称")
        XN=input()
        if XN.strip()=="":
            print("\033[91m输入不能为空，请重新输入！\033[0m")
            print("\n\033[34m按任意键返回主菜单...\033[0m")
            input()
            main()
        XNData=re.findall(r"!—{5,}\s"+XN+r".*?!—{5,}",read,re.DOTALL)
        if not XNData:
            print(f"\033[91m未找到外设{XN}的函数列表，请检查输入是否正确！\033[0m")
        if XNData:
            print(f"\n\n\033[92m{XN}函数列表如下：\033[0m")
            for i in XNData:
                print(i)
    print("\n\033[34m按任意键返回主菜单...\033[0m")
    input()
    main()

#模式3
def Mode3():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"\n\033[91m❌ 错误：未找到文件「{file_path}」！\033[0m")
        print("\033[91m请检查文件是否存在，或文件路径是否正确。\033[0m")
        print("\n\033[34m按任意键返回主菜单...\033[0m")
        input()
        main()
    UIA=re.findall(r"—{6,}!!.*?—{6,}!!",read,re.DOTALL)
    for i in UIA:
        print(i)
    print(f"\n\n\033[92m是否要单独查看某个引脚的信息？(Y/N)\033[0m")
    unn=input()
    if unn in ["Y"]:
        print(f"\033[92m输入引脚名，将返回引脚相关信息：\033[0m")
        YN=input()
        if YN.strip()=="":
            print("\033[91m输入不能为空，请重新输入！\033[0m")
            print("\n\033[34m按任意键返回主菜单...\033[0m")
            input()
            main()
        YNData1=re.findall(r"#{5,}！\s引脚名称：" + re.escape(YN) + r"\s.*?#{5,}！",read,re.DOTALL)
        if not YNData1:
            print(f"\033[91m未找到与{YN}相关的引脚信息，请检查输入是否正确！\033[0m")
        else:
            print(f"\n\n\033[92m与{YN}相关的引脚信息如下：\033[0m")
            for i in YNData1:
                print(i)
    
    print("\n\033[34m按任意键返回主菜单...\033[0m")
    input()
    main()




main()

