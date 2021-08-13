"""
file_path = "digit.txt"
with open(file_path,'r') as number:
    contents = number.read().rstrip()
    print(contents)
print("-"*35)
file_path1 = "digit.txt"
with open(file_path1,'r') as number1:
    for line in  number1:
        line1= line.strip()
        print(line1)
    print("&"*30)
file_path1 = "digit.txt"
with open(file_path1, 'r') as number1:
    contents1 = number1.readline().rstrip()
    print(contents1)
    print("*"*30)
file_path1 = "digit.txt"
with open(file_path1,'r') as number1:
    contents2 =  number1.readlines()
    for line2 in contents2:
        print(line2.rstrip())
    print("*"*30)
with open(file_path1, 'r') as number1:
    contents2 = number1.readlines()
string = ""
for line2 in contents2:
       string += line2.rstrip()
print(string)
print(len(string))

# birthday = input("Plese enter your birthday:")
# if birthday in string:
#     print("你的生日出现在这个序列中")
# else:
#     print("你的生日不再这个序列中")
# file1 = "Code.txt"
# with open(file1,"w") as a:
#     a.write("I like movie and football, \n")
#     a.write("I like music and basketball, \n")
# with open(file1,"a") as a:
#     a.write("I like beautiful and scenary, \n") # "r"只读模式，不声明默认不加
"""
'''
file_name = "Code.txt"
try:
    with open(file_name) as fl:
        cotent = fl.read()
except FileNotFoundError:
    print("Sorry,你要找的文件不存在")
else:
    numbers1 = cotent.split()
    num1 = len(numbers1)
print("The file "+ file_name+"is about "+ str(num1)+ " word")
'''

def Count_Word(file_name):
    "计算一个文件的字数"
    try:
        with open(file_name) as fl:
            cotent = fl.read()
    except FileNotFoundError:
        print("Sorry,你要找的文件不存在")
    else:
        numbers1 = cotent.split()
        num_word = len(numbers1)
        print("The file " + file_name + "is about " + str(num_word) + " word")
file_name = ["digit.txt","Code.txt","liu.txt","jiang.txt","wu.txt"]
for num in file_name:
    Count_Word(num)
