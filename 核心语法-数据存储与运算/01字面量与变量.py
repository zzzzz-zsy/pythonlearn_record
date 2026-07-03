# 字面量的写法
# 字面量：指程序中，直接书写的固定值（数据），就称为字面量
# 字面量类型及书写格式：
# 数字类型：包括整数（int）：10，18，-5，0；浮点数/小数（float）：8.5 3.14 1.0
# 布尔（bool）：表达现实生活中的逻辑，真或假 True（1） False（0） 首字母要大写 本质也是数字类型中的整型
# 字符串（str）：描述文本的一种数据类型：“人生苦短，我用python” 必须使用双引号
# 空值（NoneType）：表示空或者无值，仅包含一个值None
# 数据容器：存储多项数据的容器：列表/元组/集合/字典
# print(100)#整数 int
# print(3.14) #浮点数/小数 float
# print(True);print(False) #布尔 bool
# print("Hello World") #字符串 str
# print("-------------") #字符串 str
# print(None) #空值 NoneType
#
# # 布尔类型本质也是整数类型
# print(True+1) # 2
# print(False+1)
from ast import increment_lineno
from inspect import AGEN_CLOSED

# 变量：程序中用来存储单个数据的容器，通常会把经常发生变化的数据存储在变量中
# 定义格式：变量名=变量的值
# = 赋值操作
# num = 120
# # python 动态类型语言，在程序运行时才进行类型检查，变脸的类型可以在程序运行过程中改变（一个变量可以接收不同类型的值）
# # 在项目中建议一个变量存储一种类型数据
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)
# num = False
# print(num)

# base = 20.7 #基础播放量 万
# incr = 50 #每个月新增播放量
# print("未来第一个月的播放总量：",base + incr)
# print("未来第二个月的播放总量：",base + incr + incr)

# # 一次性定义多个变量
# base ,incr = 20.7,50
# print("未来第一个月的播放总量：",base + incr)
# print("未来第二个月的播放总量：",base + incr + incr)

# a = 10
# b = 20
# print(a)
# print(b)
#
# c = a
# a = b
# b = c
# print(a)
# print(b)
# a , b , c = 100,200,300
# print(a,b,c)
# b_temp = b
# c_temp = c
# c = a
# a = b_temp
# b = c_temp
# print(a,b,c)
#
# # 另一种只需要新增一个变量的方法： a b temp c
# a , b , c = 100,200,300
# temp = c
# c = a
# a = b
# b = temp
# print(a,b,c)
#
# # a temp b c
# a , b , c = 100,200,300
# temp = b
# b = c
# c = a
# a = temp
# print(a,b,c)
#
# # 循环移位思想 temp a b c
# a , b , c = 100,200,300
# temp = a
# a = b
# b = c
# c = temp
# print(a,b,c)

a , b , c = 100,200,300
c ,a ,b =a ,b ,c
print(a,b,c)

