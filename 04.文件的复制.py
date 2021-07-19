# 打开源文件和打开需要的文件（注：赋值的文件不存在，需要新建）
"""
file_txt = open("love.txt",'r', encoding="utf-8")
file1_txt = open("love.txt[副本]",'w', encoding="utf-8") # 此文件打开方式需要只写方式

# 读取file_txt文件的内容；将读取的内容写入到file1_txt文件中。
txt1 = file_txt.read()
file1_txt.write(txt1)

# 关闭两个文件
file_txt.close()
file1_txt.close()
# 以上代码是对于小文件的复制
"""
'''
下面是对于大文件的复制方法
'''
"""
file_txt = open("love.txt",'r', encoding="utf-8")
file1_txt = open("love.txt[副本1]",'w', encoding="utf-8")
# 依次按行读取源文件，使用while Ture死循环且需要推出判断是否读取完毕，从而跳出死循环。
while True :
    txt1 = file_txt.readline()
    file1_txt.write(txt1)
    if len(txt1) == 0:
        break
# 关闭文件
file_txt.close()
file1_txt.close()
"""
# 重命名和删除文件：os.rename("mingzi1", "mingzi2") 和os.remove("wenjianming")
# import os
# # os.rename("love.txt[副本1]" , "love1.txt")
# os.remove("love.txt[副本]") #不在该目录下就需要填写文件所在路径