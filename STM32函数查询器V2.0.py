import re
from rich.console import Console
from rich.panel import Panel
from rich import print
console = Console()
file_path = "stm32f103c8t6_@.txt"


Panel1=Panel("[bold green]**************************欢迎使用STM32查询系统V2.0*****************************[/bold green]\n[blink yellow]***********************本程序由广西科技大学  @一岁  编写*************************[/blink yellow]\n[italic red]注：本程序仅支持STM32F103C8T6相关函数的查询[/italic red]", title="【欢迎界面】", border_style="green", expand=False)
console.print(Panel1)

def main():
    #模式选择：
    #panel2 = Panel("[blink green][1][/blink green] 输入函数名查找函数\n[blink green][2][/blink green] 查看函数名\n[blink green][3][/blink green] 查询STM32F103C8T6的引脚定义\n[blink green][4][/blink green] 外设开启和运用\n[blink green][5][/blink green] 其他内容", title="【模式选择】", border_style="blue", expand=False)
    panel2 = Panel("[blink green][1][/blink green] 输入函数名查找函数\n[blink green][2][/blink green] 查看函数名\n[blink green][3][/blink green] 查询STM32F103C8T6的引脚定义\n[blink green][4][/blink green] 外设开启和运用", title="【模式选择】", border_style="blue", expand=False)
    console.print(panel2)
    Mode=input()
    Cha(Mode)
    if Mode=="1":
        Mode1()
    if Mode=="2":
        Mode2()
    if Mode=="3":
        Mode3()
    if Mode=="4":
        Mode4()
    if Mode=="5":
        Mode5()
    if Mode not in ["1","2","3","4","5"]:
        print("[bold red]输入错误，请重新选择模式！[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()

#模式1
def Mode1():
    #函数查找：
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"[bold red]❌ 错误：未找到文件「{file_path}」！[/bold red]")
        print("[bold red]请检查文件是否存在，或文件路径是否正确。[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()
    DU=open(file_path,encoding="utf-8")
    read=DU.read()
    print("[bold green]请输入要查找的函数名：[/bold green]")
    HanShu=input()
    Cha(HanShu)
    Cha(HanShu)
    if HanShu.strip()=="":
        print("[bold red]输入不能为空，请重新输入！[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()
    UI=r"—{10,}\s函数名："+HanShu+r".*?—{10,}"
    Data=re.findall(UI,read,re.DOTALL)
    if not Data:
        print(f"[bold red]未找到函数[/bold red][bold blue]{HanShu}[/bold blue][bold red]，请检查输入是否正确！[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()
    if Data:
        CI=[]
        print(f"\n\n[bold green]{HanShu}函数查找结果如下[/bold green]")
        for i in Data:
            Panel3=Panel(i,title=f"【{HanShu}函数信息】", border_style="green", expand=False)
            console.print(Panel3)
        for i in Data:
            un=re.findall(r"输入参数[0-9]+：([^：]+)：",i,re.DOTALL)
            #如果有参数
            if un:
                CI.append(un)
                for j in CI:
                    print("[bold green]参数查询如下：[/bold green]")
                    for k in j:
                        InitTypeDef=re.findall("InitStruct",k,re.DOTALL)
                        asj = re.findall(r"—{5,}\s*"+re.escape(k)+r".*?—{5,}",read, re.DOTALL)
                        if not InitTypeDef:
                            if not asj:
                                print(f"[bold red]未找到参数{k}的详细信息！[/bold red]")
                            if asj:
                                for l in asj:
                                    print(l)
                        if InitTypeDef:
                            CCAD=re.findall(r"([^：]+)_",k,re.DOTALL)
                            for m in CCAD:
                                CHi=re.findall(r"—{5,}\s*"+m+r"_InitTypeDef.*?#{5,}",read,re.DOTALL)
                                if not CHi:
                                    print(f"[bold red]未找到参数{k}的详细信息！[/bold red]")
                                if CHi:
                                    for n in CHi:
                                        print(n)
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()

#模式2
def Mode2():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"[bold red]❌ 错误：未找到文件「{file_path}」！[/bold red]")
        print("[bold red]请检查文件是否存在，或文件路径是否正确。[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        input()
        main()
    XData=re.findall(r"#{10,}\s!—{5,}\sADC.*?#{10,}",read,re.DOTALL)
    print(f"\n\n[bold green]函数列表如下：[/bold green]")
    for i in XData:
        Panel1=Panel(i,title=f"【函数列表】", border_style="green")
        console.print(Panel1)
    print(f"\n[bold green]是否要单独查看某个外设的函数列表？(Y/N)[/bold green]")
    YN=input()
    Cha(YN)
    if YN in ["Y"]:
        print("\n\n[bold green]请输入要查看的外设名称：[/bold green]")
        print("可输入：ADC、GPIO、USART等外设名称")
        XN=input()
        Cha(XN)
        if XN.strip()=="":
            print("[bold red]输入不能为空，请重新输入！[/bold red]")
            print("[bold blue]按任意键返回主菜单...[/bold blue]")
            qq=input()
            Cha(qq)
            main()
        XNData=re.findall(r"!—{5,}\s"+XN+r".*?!—{5,}",read,re.DOTALL)
        if not XNData:
            print(f"[bold red]未找到外设{XN}的函数列表，请检查输入是否正确！[/bold red]")
        if XNData:
            print(f"\n\n[bold green]{XN}函数列表如下：[/bold green]")
            for i in XNData:
                Panel1=Panel(i,title=f"【{XN}函数列表】", border_style="green", expand=False)
                console.print(Panel1)
    print("\n[bold blue]按任意键返回主菜单...[/bold blue]")
    qq=input()
    Cha(qq)
    main()

#模式3
def Mode3():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"[bold red]❌ 错误：未找到文件「{file_path}」！[/bold red]")
        print("[bold red]请检查文件是否存在，或文件路径是否正确。[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        input()
        main()
    UIA=re.findall(r"—{6,}!!.*?—{6,}!!",read,re.DOTALL)
    for i in UIA:
        Panel1=Panel(i,title=f"【引脚定义表】", border_style="green")
        console.print(Panel1)
    print(f"\n\n[bold green]是否要单独查看某个引脚的信息？(Y/N)[/bold green]")
    unn=input()
    Cha(unn)
    if unn in ["Y"]:
        print(f"[bold green]输入引脚名，将返回引脚相关信息：[/bold green]")
        YN=input()
        Cha(YN)
        if YN.strip()=="":
            print("[bold red]输入不能为空，请重新输入！[/bold red]")
            print("[bold blue]按任意键返回主菜单...[/bold blue]")
            qq=input()
            Cha(qq)
            main()
        YNData1=re.findall(r"#{5,}！\s引脚名称：" + re.escape(YN) + r"\s.*?#{5,}！",read,re.DOTALL)
        if not YNData1:
            print(f"[bold red]未找到与{YN}相关的引脚信息，请检查输入是否正确！[/bold red]")
        else:
            print(f"\n\n[bold green]与{YN}相关的引脚信息如下：[/bold green]")
            for i in YNData1:
                Panel1=Panel(i,title=f"【{YN}引脚信息】", border_style="green", expand=False)
                console.print(Panel1)
    
    print("[bold blue]按任意键返回主菜单...[/bold blue]")
    qq=input()
    Cha(qq)
    main()

def Mode4():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"[bold red]❌ 错误：未找到文件「{file_path}」！[/bold red]")
        print("[bold red]请检查文件是否存在，或文件路径是否正确。[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
    print(f"\n[bold green]请输入要查询的外设名称：[/bold green]")
    WAI=re.findall(r"—{5,}WAI.*?—{5,}WAI",read,re.DOTALL)
    for i in WAI:
        Panel1=Panel(f"[blink]{i}[blink]",title=f"[bold blue]【STM32F103C8T6外设列表】[/bold blue]", border_style="green", expand=False)
        console.print(Panel1)
    YN=input()
    Cha(YN)
    if YN.strip()=="":
        print("[bold red]输入不能为空，请重新输入！[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
        main()
    YNData=re.findall(r"—{5,}！！！\s"+YN+r".*?—{5,}！！！",read,re.DOTALL)
    if not YNData:
        print(f"[bold red]未找到外设{YN}的相关信息，请检查输入是否正确！[/bold red]")
    if YNData:
        print(f"\n\n[bold green]{YN}相关信息如下：[/bold green]")
        for i in YNData:
            BUZHOU0=re.findall(r"—{5,}！！！\s.*?—{2,}1",i,re.DOTALL)
            BUZHOU1=re.findall(r"—{5,}1\s.*?—{5,}2",i,re.DOTALL)
            BUZHOU2=re.findall(r"—{5,}2\s.*?—{5,}3",i,re.DOTALL)
            BUZHOU3=re.findall(r"—{5,}3\s.*?—{5,}4",i,re.DOTALL)
            BUZHOU4=re.findall(r"—{5,}4\s.*?—{5,}5",i,re.DOTALL)
            BUZHOU5=re.findall(r"—{5,}5\s.*?—{5,}6",i,re.DOTALL)
        if BUZHOU0:
            for i in BUZHOU0:
                BUZHOU0_1=re.findall(r"—{5,}！！！\s"+YN+r".*?##",i,re.DOTALL)
                BUZHOU0_2=re.findall(r"!##\s.*?—{2,}1",i,re.DOTALL)
        if BUZHOU1:
            for i in BUZHOU1:
                BUZHOU1_1=re.findall(r".*?##",i,re.DOTALL)
                BUZHOU1_2=re.findall(r"!##\s.*?—{2,}2",i,re.DOTALL)
        if BUZHOU2:
            for i in BUZHOU2:
                BUZHOU2_1=re.findall(r".*?##",i,re.DOTALL)
                BUZHOU2_2=re.findall(r"!##\s.*?—{2,}3",i,re.DOTALL)
        if BUZHOU3:
            for i in BUZHOU3:
                BUZHOU3_1=re.findall(r".*?##",i,re.DOTALL)
                BUZHOU3_2=re.findall(r"!##\s.*?—{2,}4",i,re.DOTALL)
        if BUZHOU4:
            for i in BUZHOU4:
                BUZHOU4_1=re.findall(r".*?##",i,re.DOTALL)
                BUZHOU4_2=re.findall(r"!##\s.*?—{2,}5",i,re.DOTALL)
        if BUZHOU5:
            for i in BUZHOU5:
                BUZHOU5_1=re.findall(r".*?##",i,re.DOTALL)
                BUZHOU5_2=re.findall(r"!##\s.*?—{2,}6",i,re.DOTALL)
        if BUZHOU0:
            if BUZHOU0_1:
                for i in BUZHOU0_1:
                    panel2 = Panel(f"[bold green]{i}[/bold green]",title=f"【{YN}介绍】", border_style="green")
                    console.print(panel2)
            if BUZHOU0_2:
                for i in BUZHOU0_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【{YN}相关注意事项】", border_style="red")
                    console.print(panel2)
        if BUZHOU1:
            if BUZHOU1_1:
                for i in BUZHOU1_1:
                    panel2 = Panel(i,title=f"_", border_style="blue")
                    console.print(panel2)
            if BUZHOU1_2:
                for i in BUZHOU1_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【相关注意事项】", border_style="red")
                    console.print(panel2)
        if BUZHOU2:
            if BUZHOU2_1:
                for i in BUZHOU2_1:
                    panel2 = Panel(i,title=f"_", border_style="blue")
                    console.print(panel2)
            if BUZHOU2_2:
                for i in BUZHOU2_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【相关注意事项】", border_style="red")
                    console.print(panel2)
        if BUZHOU3:
            if BUZHOU3_1:
                for i in BUZHOU3_1:
                    panel2 = Panel(i,title=f"_", border_style="blue")
                    console.print(panel2)
            if BUZHOU3_2:
                for i in BUZHOU3_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【相关注意事项】", border_style="red")
                    console.print(panel2)
        if BUZHOU4:
            if BUZHOU4_1:
                for i in BUZHOU4_1:
                    panel2 = Panel(i,title=f"_", border_style="blue")
                    console.print(panel2)
            if BUZHOU4_2:
                for i in BUZHOU4_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【相关注意事项】", border_style="red")
                    console.print(panel2)
        if BUZHOU5:
            if BUZHOU5_1:
                for i in BUZHOU5_1:
                    panel2 = Panel(i,title=f"_", border_style="blue")
                    console.print(panel2)
            if BUZHOU5_2:
                for i in BUZHOU5_2:
                    panel2 = Panel(f"[bold yellow]{i}[/bold yellow]",title=f"【相关注意事项】", border_style="red")
                    console.print(panel2)

    print("[bold blue]按任意键返回主菜单...[/bold blue]")
    qq=input()
    Cha(qq)
    main()

def Mode5_1(x,read):
    if x=="1":
        I2CData=re.findall(r"—{5,}I2C.*?—{5,}I2C",read,re.DOTALL)
        for i in I2CData:
            Panel1=Panel(i,title=f"【I2C通信协议详解及STM32F103C8T6软件模拟实现】", border_style="green")
            console.print(Panel1)

def Mode5():
    try:
        with open(file_path, encoding="utf-8") as DU:
            read= DU.read()
    except FileNotFoundError:
        print(f"[bold red]❌ 错误：未找到文件「{file_path}」！[/bold red]")
        print("[bold red]请检查文件是否存在，或文件路径是否正确。[/bold red]")
        print("[bold blue]按任意键返回主菜单...[/bold blue]")
        qq=input()
        Cha(qq)
    panel2 = Panel("[blink green][1][/blink green] I2C介绍和软件I2C的编写", title="[bold green]【选择要查看的内容】[/bold green]", border_style="blue", expand=False)
    console.print(panel2)
    Mo=input()
    Cha(Mo)
    Mode5_1(Mo,read)
    if Mo not in ["1"]:
        print("[bold red]输入错误，请重新选择内容！[/bold red]")
    print("[bold blue]按任意键返回主菜单...[/bold blue]")
    qq=input()
    Cha(qq)
    main()


#/跳转
def Cha(Zhi):
    Da=re.findall(r"/",Zhi,re.DOTALL)
    if Da:
        print("\n\n[blink yellow]##跳转模式##[/blink yellow]")
        Da1=re.findall(r"/[1-5]",Zhi,re.DOTALL)
        if not Da1:
            print(f"[bold red]跳转输入错误，请重新输入[直接按回车返回主菜单]！[/bold red]")
            Cha(input())
        if Da1:
            if Da1[0]=="/1":
                Mode1()
            if Da1[0]=="/2":
                Mode2()
            if Da1[0]=="/3":
                Mode3()
            if Da1[0]=="/4":
                Mode4()
            if Da1[0]=="/5":
                Mode5()
        main()
            







main()