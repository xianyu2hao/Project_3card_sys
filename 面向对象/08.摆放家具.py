# 家具摆放案例
'''
家具类(Item)具体 对象
席梦思(bed) 占地 4 平米
衣柜(chest) 占地 2 平米
餐桌(table) 占地 1.5 平米
家具类：(HouseItem)
名字-->属性(name)
占地-->属性(Item_area)

房子类(House)
户型（House_type）
总面积(area)

家具名称列表(Item_list)
剩余面积(free_area)
添加家具(Add_Iterm)
'''
class HouseItem:
    """家具类"""
    def __init__(self,name,area):
        """初始化方法"""
        self.name = name
        self.Item_area = area
    def __str__(self):
        """输出对象的描述信息"""
        return "家具名称：%s，占地面积：%s"%(self.name,self.Item_area)
# 由类创建对象
bed = HouseItem("席梦思",4)
print(bed)
print(bed.name)
print(bed.Item_area)
#
# chest = HouseItem("衣柜",2)
# print(chest)
#
# table = HouseItem("餐桌",1.5)
# print(table)
# 房子类
class House:
    """房子类"""
    def __init__(self,House_type,area,):
        """初始化方法"""
        self.House_type = House_type
        self.House_area = area
        self.free_area = area
        self.House_Item = []
    def __str__(self):
        """"打印房子对象描述信息"""

        return ("户型：%s，总面积：%.1f米，剩余面积：%.1f米，家具名称列表：%s") % (self.House_type,self.House_area,self.free_area,self.House_Item)
    def Add_Item(self,Item):
        """添加家具的方法"""
        if self.free_area <  self.Item.area:
            print("哎呀，添加的%s家具面积太大，无法添加！！！")
            return
        self.free_area -= self.Item.area
        self.House_Item.append(Item.name)

# 由类创建房子对象
big_house = House("大别墅",60)
print(big_house)

# 房间内添加席梦思
big_house.Add_Item(bed)
print(big_house)
