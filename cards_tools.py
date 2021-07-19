# 负责各个功能函数的实现和定义
# 但是不能调用各个功能，需要由总控中心
# 实现功能：显示菜单、新建名片、显示全部名片、查询名片、修改名片、删除明显、返回上一级
# coding:utf-8
# 定义菜单显示函数
import  os
# 1.菜单栏函数
def show_menu():
    """
    定义显示菜单函数
    :return:
    """
    print("")
    print("*" * 50)
    print("欢迎使用 [名片管理系统] v1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("0. 退出系统")
    print("")
    print("*" * 50)

# 新建名片功能函数
card_list = [
'''
 {'name':"小郭",'phone':"100865",'qq':"1234564",'email':"152454@qq.com"}
 {'name':"小王",'phone':"1015865",'qq':"123415564",'email':"1524154154@qq.com"}  {'name':"小张",'phone':"11234855",'qq':"59874144",'email':"152454@163.com"} 
'''
]
# 2.新建名片函数
def new_card():
    """
    新建名片函数
    :return:
    """
    print("[功能]新建名片")
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ号：")
    email_str = input("请输入邮箱：")
    new_dict = {'name': name_str, 'phone': phone_str, 'qq': qq_str, 'email': email_str}
    card_list.append(new_dict)
    print("新建姓名是:%s名片成功！" % name_str)
    # print(card_list)


# 3.显示全部名片功能函数
def show_all():
    """
    显示全部名片
    :return:
    """
    # 先判断列表有没有数据，选择执行或者不执行；return除了返回值还可以提前终止函数运行
    if len(card_list) <= 0:
        print("当前名片没有数据，请新建名片！")
        return
    print("[功能]显示全部")
    print("-" * 50)
    print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮箱".ljust(10), sep='\t\t')
    for item in card_list:  # 临时变量获取的是列表中的字典
        print(item.get('name').ljust(10), item.get('phone').ljust(10), item.get('qq').ljust(10),
              item.get('email').ljust(10), sep='\t\t')
    print("-" * 50)


# pass是占位符，完善语法作用，不输出任何内容,但是也占用资源。
# 当前代码待完成
# 4.查询名片功能函数
def search_card():
    """
    实现查询名片的功能
    :return:
    """
    print("[功能]查询名片")
    find_name = input("请输入您要查询的姓名:")  # 获取查询的姓名
    # 获取的姓名在列表中查询，是否在列表中存在
    for item in card_list:
        if item.get('name') == find_name:
            print("已经找到姓名为：%s 的名片" % item.get('name'))
            print("-" * 50)
            print("姓名".ljust(10), "电话".ljust(10), "QQ号".ljust(10), "邮".ljust(10), sep='\t\t')
            print("-" * 50)
            print(item.get('name').ljust(10), item.get('phone').ljust(10), item.get('qq').ljust(10),item.get('email').ljust(10), sep='\t\t')
            deal_card(item)
            break
    else:
        print("没有找到姓名为：%s 的名片，请核对后重新输入!!！" % find_name)
# 5.对调用的函数进行选择操作
def deal_card(find_dict):
    """
    选择1是修改名片
    选择2是删除名片
    选择0是返回上一级
    输入是其他的，提示输入有误，重新输入
    :return:
    """
    op = input("请输入对名片的操作选择[1.修改  2.删除  0.返回上一级]:")
    if op == "1":
        print("[功能]修改名片")
        # 获取修改后的姓名 电话 QQ号 邮箱，然后进行修改
        change_name = input_card(find_dict.get('name'),"请输入修改后的姓名[不修改直接回车]:")
        change_phone = input_card(find_dict.get('phone'),"请输入修改后的手机[不修改直接回车]:")
        change_qq = input_card(find_dict.get('qq'),"请输入修改后的qq号[不修改直接回车]:")
        change_email = input_card(find_dict.get('email'),"请输入修改后的邮箱[不修改直接回车]:")
        # 此处可以将chage的几个临时变量直接删除，让find.dict['name']=input_card..get('name'),"请输入修改后的姓名[不修改直接回车]:")
        find_dict['name'] = change_name
        find_dict['phone'] = change_phone
        find_dict['qq'] = change_qq
        find_dict['email'] = change_email
        print("修改名片成功！")
    elif op == "2":
        print("[功能]删除名片")
        card_list.remove(find_dict)
        print("删除成功！")
    elif op == "0":
        print("[功能]返回上一级")
        return
    else:
        print("输入有误，请核对后重新输入！！！")
#6.
def input_card(find_dict,msg): # 对input函数进行扩充
    info = input(msg)
    if len(info) > 0:
        print(info)
        return (info)
    else:
        return (find_dict)
# 7.将输入文件系统的内容保存到文件数据中
def save_card_data():
    # 将输入的文件放入文件管理系统的文件数据中
    card_file_txt= open("card_data.txt","w",encoding="utf-8")
    # 将输入的名片列表的数据输入到文件中
    card_file_txt.write(str(card_list)) # 不能将列表直接写入文件，需要转换为字符串
    card_file_txt.close()
# 确保下次启动可以导入之前保存的数据

# 8.下次再启动文件管理系统读取到名片列表中
def load_files_data():
    # 判断文件存不存在
    if  os .path.exists("card_data.txt"):
      # 打开文件
        card_file= open("card_data.txt","r",encoding="utf-8")
      # 操作文件
        card_files1 = card_file.read()
        if len(card_files1) == 0:
            print("当前card_data.txt文件内容为空！")
            card_file.close()
            return
        # 将列表修改为全局变量
        global card_list
        card_list = eval(card_files1)  # 读取的是字符串，不能直接装进列表中，需要eval()函数转换；另外eval函数执行空会错误，故需要先判断
        # 关闭文件
        card_file.close()
    else:
        print("保存名片列表不存在，请新建！")