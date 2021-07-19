# Cat
# eat
# drink
# 定义 类 模板
class Cat:
    """猫类"""
    def eat(self):
        """吃方法"""
        print("__小猫爱吃鱼__",self)
    def drink(self):
        """喝方法"""
        print("__小猫想喝水__",self)

# 使用 类 创建对象
# 对象变量= 类名（）
Tom = Cat()
# 调用 格式：对象名.方法名（参数）
Tom.eat()
print("_"*30)

Bai = Cat()
Bai.drink()
# 同一个类 创建的不同的对象，那么对象也储存在不同的物理地址，由self参数可知；然后使用的是引用地址。