# 当前python作为模块
# 全局变量
g_str= "hello world"

# 函数
def fun():
    print("___model2的输出函数被调用___")

# 类
class Cat:
    def __init__(self):
        self.name = "大懒猫"

    def eat(self):
        print("%s爱吃米饭饭"% self.name)