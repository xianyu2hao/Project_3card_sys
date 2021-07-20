# 导入模块
import model_1
import model_2  as MH2

# 还可以使用（from 模块名 import 工具名 ）调用这个具体的工具（全局变量，函数，类等）
# 使用模块中的工具：调用
# 全局变量:模块名+变量名
print(model_1.g_num)
print(MH2.g_str)

# 模块名+函数名
model_1.fun()
MH2.fun()

# 模块名+类名
model_1.Cat()
cat = MH2.Cat()
cat.eat()
