# 私有方法和私有属性：在对象内部被使用，不希望外部使用
class Women:
    """美女类"""
    def __init__(self,name):
        """初始化方法"""
        self.name = name
        self.__age = 20

    # 如需要访问私有属性，则需要提供访问私有属性的；对外提供get/set访问接口
    def get_age(self):
        """获取私有属性"""
        return self.__age

    def set_age(self,new_age):
        """设置私有属性值"""
        if new_age <= 0 or new_age >= 150:
            print("年龄有误，请重新输入")
            return
        self.__age = new_age

    # 如需要访问私有属性，则需要提供访问私有属性的；对外提供get/set访问接口
    def eat(self):
        """吃方法"""
        print("%s是一个吃货" % self.name)
        # print("%s是一个吃货，今年%s岁"% (self.name,self.__age)) # 在类的内部通过self访问私有属性
        # self.__secret()  # 在类的内部通过self访问私有方法
    def __secret(self):  # 前置双下划线的属于私有方法
        print("不开放个人秘密，禁止访问")

# 由类创建模板
ruhua = Women("如花")
print(ruhua.name)
# print(ruhua.__age)   # 类的外部无法直接访问私有属性
ruhua.eat()
# ruhua.__scret( )    # 类的外部无法直接访问私有方法

# pthon中没有真正的私有，这种私有是伪私有
# print(dir(ruhua))
# print(ruhua._Women__age)
# ruhua._Women__secret()
print(ruhua.get_age())
ruhua.set_age(25)
print(ruhua.get_age())