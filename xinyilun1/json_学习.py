# import json
# names = [1,2,3,1,5]
# filename = "name.json"
# with open(filename,"w") as text:
#     json.dump(names,text)
# import json
# filename = "name.json"
# with open(filename) as text:
#     name1 = json.load(text)
# print(name1)
import json
file_name = "name.json"
try:
    with open(file_name) as name1:
        name2 = json.load(name1)
except FileNotFoundError:
    name2 = input("您叫什么名字？")
    file_name = "name.json"
    with open(file_name,"w") as name1:
        json.dump(name2,name1)
        print("我会记得你的，欢迎回来！")
else:
    print("欢迎回来"+name2)





