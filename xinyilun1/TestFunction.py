from Name_Function import get_fomatted_name
print("按 q 键推出！")
while True:
    first = input("\n请输入你的姓氏:")
    if first == "q":
        break
    last =input("请输入您的名字:")
    if last == "q""" :
        break
    formatted_name = get_fomatted_name(first,last)
    print("\t你的姓名为："+formatted_name+".")