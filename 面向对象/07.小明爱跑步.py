class Person:
    """人类"""
    def __init__(self,name,weight):
        """初始化方法"""
        self.name = name
        self.weight = weight
    def __str__(self):
        """打印对象的描述信息"""
        return "姓名是：%s，体重是：%.2f公斤"%(self.name,self.weight)
    def run(self):
        """跑方法"""
        print("%s爱减肥,每次跑步减去0.5公斤"% self.name)
        self.weight -= 0.5  # 相当于self.weight=self.weight-0.5
    def eat(self):
        """吃方法"""
        print("%s爱吃东西，每次吃东西增加1公斤"% self.name)
        self.weight += 1 #相当于self.weight=self.weight+1

xiaoming = Person("小明",75.0)
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)
print("_"*35)
xiaomei = Person("小美",45.0)
print(xiaomei)
xiaomei.run()
print(xiaomei)
xiaomei.eat()
print(xiaomei)