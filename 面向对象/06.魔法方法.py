'''
# __del__方法；程序退出时，对象从内存空前销毁前自动调用，清除资源的操作
# 注意格式对其，不然报错
class Cat:
    def __init__(self,name):   #初始化方法
        self.name = name
    def eat(self):
        """吃方法"""
        print("%s爱吃鱼" % self.name)
    def __del__(self):
        """删除魔法方法"""
        print("清除资源的操作")

tom = Cat("汤姆猫")
tom.eat()
del tom
print(tom.name)
'''
 # __str__方法；必须返回一个字符串；打印对象时，自动调用；格式：print(对象)，__str__()
class Cat:
    def __init__(self,name):   #初始化方法
        self.name = name
    def eat(self):
        """吃方法"""
        print("%s爱吃鱼" % self.name)
    def __str__(self):
        """对象的描述信息"""
        print("使用打印对象时，自动调用")
        return ("名字是：%s"% self.name)
tom = Cat("汤姆猫")
print(tom)
