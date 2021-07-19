# 程序运行中，有些错误程序员不能处理（如网络差），为了让程序继续执行，就需要对异常代码进行处理
# 捕获异常；对于一些代码不确定是否能够正确执行，可用 try(尝试)来捕获

# try:
#     int("num")
#     print("可能出现异常的代码")
# except:
#     print("已经捕获到异常，执行这部分")
# # try部分出现多个异常，只能捕获第一个异常

# 捕获指定 类型 的异常：报错信息最后一行的第一个单词
'''
try:
    # int("num")
    print("可能出现异常的代码")
    # x = 1/0
    # name = 0
    print(name)
except ValueError :
    print("已经捕获到值异常，执行这部分")
except ZeroDivisionError:
    print("已经捕获到0分母异常，执行这部分")
except NameError:
    print("已经捕获到名字错误异常，执行这部分")
'''
print("_"*40)

# 一次捕获多个异常；格式： except (类型1，类型2，类型3,...类型n):
# 对不同类型的异常，都有相同的处理结果（因为异常类型太多，不能穷举，故这种比较不方便）


'''
#使用'任意类型的异常'，格式except Exception:
try:
    # int("num")
    print("可能出现异常的代码")
    # x = 1/0
    # name = 0
    print(name)
except Exception as  exp:
    print("已经捕获到异常，执行这部分", exp)
'''
# 异常的完整语法
"""
格式：
try
    可能出现异常的代码
except 异常类型1：
    针对异常类型1的处理代码
except 异常类型2：
    针对异常类型2的处理代码
except （异常类型3，异常类型4）：
    针对异常类型3或异常类型4的处理代码
except Exception as exp: # exp获取异常部分的信息
    针对其他异常类型的处理代码
else:
    没有发生异常时，执行的代码
finally：
    无论有没有错误都会执行的代码
"""

'''
try:
    # int("num")
    print("可能出现异常的代码")
    # x = 1/0
    # name = 0
    print(name)
except ValueError :
    print("已经捕获到值异常，执行这部分")
except ZeroDivisionError:
    print("已经捕获到0分母异常，执行这部分")
except NameError as  exp:
    print("已经捕获到名字错误异常，执行这部分",exp)
else:
    print("无异常，就一定会执行的代码")
finally:
    print("无论有没有异常都会执行的代码")
    
'''
# 抛出异常
# 1.提示用户输入密码；密码长度小于8抛出异常；3.密码长度大于等于8继续执行,返回密码
def pass_word():
    pwd = input("请输入密码[密码长度不小于8位]：")
    if len(pwd) < 8:
        #print("抛出异常")
        # 使用Exception类创建对象，Exception(“错误提示信息”)
        ex = Exception("错误：密码长度小于8位")
        # 使用raise抛出异常对象
        raise ex
    else:
        return pwd
try:
    pwd = pass_word()
    print(pwd)
except Exception as exp:
    print(exp)
