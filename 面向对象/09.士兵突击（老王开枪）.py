'''
士兵类：
姓名
枪
开火
'''

class Gun:
    """枪支类"""
    def __init__(self,type):
        self.type = type
        self.bullet_count = 0 # 子弹数量，新枪默认无子弹

    # 添加子弹的方法
    def add_bullet(self,count):
        """添加子弹方法"""
        self.bullet_count += count

    def shoot(self):
        """射击方法"""
        # 判断有没有子弹，没有子弹不能射击，提示添加子弹,代码不再运行
        if self.bullet_count == 0:
            print("开玩笑，无子弹怎么打枪，赶紧加子弹")
            return
        # 若有子弹怎么可以开枪，剩余子弹数量显示
        self.bullet_count -= 1
        print("%s哒达哒哒哒biubiu....剩余子弹%d颗 " % (self.type,self.bullet_count))

ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()
# ak47.shoot()


class  Sodier:
    """士兵类"""
    # gun = None 缺省参数，带有默认值的参数，None表示空，什么都没有
    def __init__(self,name,gun = None):  # 此处的gun保存的是上面Gun类创建的ak47的引用地址
        """初始化方法"""
        self.name =name
        self.gun = gun

    def add_bullet0(self,new_count):
        """士兵拿枪添加子弹和上面不同"""
        # 判断有没有枪，无枪则不能开火。提示装备枪支
        # if self.gun == None:
        if self.gun is None:
            print("%s士兵无枪，请分配枪支"% self.name)
            return
        # 若有枪则需要添加子弹
        self.gun.add_bullet(new_count)  # 此处调用的是上述Gun添加子弹的方法

    def fire(self):  # 开火方法
        # 判断有没有枪，无枪则不能开火。提示装备枪支
        # 若有枪则需要添加子弹
        # if self.gun == None:
        if self.gun is None:
            print("%s士兵无枪，请分配枪支"% self.name)
            return
        # self.gun.add_bullet(50)
        self.gun.shoot()  # 此时士兵射击子弹数量调用的是Gun的射击的方法

# 由类创建对象
LX = Sodier("许三多",ak47)
LX.add_bullet0(50)
while True:
    LX.fire()
    if ak47.bullet_count <= 38:
        break
