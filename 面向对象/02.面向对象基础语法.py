# dir 内置函数
# 定义简单的类
# 方法中的 self 函数
# 初始化方法

# 定义 类 模板
class Person:
    def run(self):
        print("--->跑<---")
    def eat(self,food):
        print("---><---",food)
    def sleep(self):
        print(">>睡觉<<")
# 根据类创建对象
# 对象变量 = 类名（）
xiaozhang = Person()
# 通过对象调用方法；格式：对象变量名.方法名（）：self参数不需要我们传递
xiaozhang.run()
xiaozhang.eat("蛋糕")

# 类 可以封装函数，比函数更大的封装；面向对象的三大特性之一是封装
