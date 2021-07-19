while True:
    print("-" * 6, end="")
    print("猜数字游戏", end="")
    print("-" * 6)
    num = input("请输入1~3之间的任意一个数：")
    if num > "3" or num < "1":
        print(
            "您的输入不正确，请检查后在输入"
        )
    else:
        import random
        ber = random.randint(1, 3)
        if ber == int (num):
            print("你赢了，你输入的值%s正确"% ber )
        elif ber < int(num):
            print("您的值大了")
        elif ber > int(num):
            print("您的值小了")
        else:
            print(
                "请再接再厉！！！"
            )
    print("-"*30)
