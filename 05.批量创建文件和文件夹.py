# 导入工具包
import os
import shutil
import  sys
# 1、批量创建文件
'''
def creat_file():
    """
    批量创建文件
    :return:
    """
    # 创建文件夹（方便查找）
    print(os.getcwd())  # 确认自己所在目录
    # 判断files目录是否存在，存在就删除，不存在就向下执行新建文件夹
    if os.path.exists("./files"):
        shutil.rmtree("./files")
    # 创建文件夹files
    os.mkdir("./files")
    # 切换到创建的文件夹目录下
    os.chdir("./files")
    # 确认自己所在目录
    print(os.getcwd())
    # 创建文件
    for i in range(1, 21):
        # print(i)
        file_txt = open("love%d.txt" % i, "w", encoding="utf-8")
        file_txt.write("两个黄鹂鸣翠柳，一行白鹭上青天。\n 窗含西岭千秋雪，门泊东吴万里船")
        file_txt.close()
creat_file()  # 记得代码编辑完要调用才能整个执行，创建文件夹和文件
'''
# 2、批量修改文件名
def change_file_name():
    # 查看是否是 files文件夹下
    print(os.getcwd())

    #若不是files目录下,切换到files目录下
    path = "D:\\Python3.9.2\Project_3\\files" # python中两个"\\"表示一个"\"
    if os.getcwd() != path :
        os.chdir(path)

    #若是files目录下,则获取该目录下所以文件列表 os.listdir()
    files_name = os.listdir()
    print(files_name)
    #for 循环遍历列表，使用os.rename()重命名
    num =1
    for name in files_name:
        os.rename(name, str(num)+ "love")
        num= num +1

change_file_name()
