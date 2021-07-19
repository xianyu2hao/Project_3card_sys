# range 函数生成一系列连续的整数，格式：range(起始位置，结束位置，步长)；可使用for循环进行遍历，另外也包括起始位置，不包括结束位置
# range(0,10,1)
# print(type(range(0,10,1)))
#
# for sun in range(0,10,1):
#     print(sun)
# laiyuan_list = ["生活缴费","行走捐","共享单车","线下支付","网络购票"]
while True:
    print("="*50)
    shuru ="查询能量请输入能量来源！退出请输入0"
    print(shuru.ljust(30))
    laiyuan = "能量来源如下:"
    print(laiyuan.ljust(30))
    fangshi = "生活缴费、行走捐、共享单车、线下支付、网络购票"
    print(fangshi.center(30))
    print("="*50)
    xingzou_str = input("请输入能量来源:")
    if "0" == xingzou_str :
        break
    else:
        # for find_str in laiyuan_list:
        if "行走捐" == xingzou_str:
                print("200g")
        elif "生活缴费" == xingzou_str:
                print("100g")
        elif "共享单车" == xingzou_str:
                print("50g")
        elif "线下支付" == xingzou_str:
                print("20g")
        elif "网络购票" == xingzou_str:
                print("10g")
        else:
                print("输入错误请重新输入！！！")

