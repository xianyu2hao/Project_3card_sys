# 有默认值的参数
def func(name,age=18, position="teacher"):
    print(name,end="")
    print(age,sep="\t")
    print(position)
func(name="张全蛋",age=25,position="Student")
