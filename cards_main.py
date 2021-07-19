# 当前文件夹是总控中心，不负责实现具体功能，负责调度各种功能函数
# 当需要调用其他.py文件需要先导入模块
import cards_tools
cards_tools.load_files_data()
while True:
    cards_tools.show_menu()
    # 成员运算符 in 的使用；作用判断一个数据是某个容器中的成员，是返回Ture，不是返回False
    # 例如 sun=[10,20,30] print(10 in sun);一般结合If条件句使用。
    # 成员运算符判断的是字典的键（KEY）
    op = input("请输入您的选择：")
    if op in ["1","2","3"]:
        if op == "1":
            #print("新建名片")
            cards_tools.new_card()
        elif op == "2":
            #print("显示全部")
            cards_tools.show_all()
        else:
            #print("查询名片")
            cards_tools.search_card()
    elif op == "0":
        print("欢迎使用名片管理系统，大哥常来玩啊")
        print(">>>>名片管理系统程序结束<<<<")
        cards_tools.save_card_data()
        break
    else:
        print("您的输入有误，请核对后重新输入")
