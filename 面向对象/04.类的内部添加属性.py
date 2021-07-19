'''
#创建类模板且内部添加属性
class Cat:
    """猫类"""
    def _init_(self): # 左边是初始化方法
        """初始化方法"""
        print("初始化的数据在这！")
        self.name ="汤姆猫"  # 此处是内部添加的属性,格式：self.属性名 = 属性值
        print("类模板中初始化后自动调用")
    def eat(self):
        print("%s吃方法"% self.name)

# 使用模板创建对象
tom = Cat()
# 访问属性
print(tom.name)
tom.eat()
print("_"*35)
# 由类创建对象2
bosimao = Cat()
# 访问属性
print(bosimao.name)
bosimao.eat()

''' # 上述方法将属性名固定了，故需要改造

# 初始化同时设置属性值
# 定义模板
class Cat:
    def __init__(self, new_name):
        self.name = new_name
    def eat(self):
        print("  %s爱吃小鱼干"% self.name)

# 创建对象1
tom = Cat("汤姆猫")
tom.eat()
# 创建对象2
bosimao = Cat("波斯猫")
bosimao.eat()

