# 字符串可以双引号定义 单引号定义 三引号定义：
# 三引号可以多行定义：
# s1 = "hello"
# s2 = 'world'
# s3 = """尊敬的客户：
#     感谢您选择我们公司的产品。
#     祝好~            """
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
from dbm import sqlite3

#定义字符串 ---> It's very good 使用转义字符
# \' 输出'
# \" 输出“
# \n 换行
# \t 制表符

# s1 = 'It\'s very good'
# print(s1)
#
# #或者双引号定义
# s2 = "It's very good"
# print(s2)
#
# s3 = ('Hello 的意思是 “您好”')
# print(s3)
#
# s4 = "欢迎光临！\n 下午好"
# print(s4)

#字符串拼接 使用（+）进行拼接
# slogan = "我是""zsy"
# print(slogan)
#
# s1 = "人生苦短"
# s2 = "及时行乐"
# print(s1 +"\n"+ s2)

#将int类型转换成字符串类型工具 str
# name = "zsy"
# age = 27
# pro = "通信工程"
# hobby = "Python"
# print("大家好,我是"+name+",今年"+str(age)+"岁,学习的专业是"+pro+",爱好"+hobby)
#
# #字符串格式化 方式1：占位符% 通过使用占位符 完成字符串和变量的快速拼接
# print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s。" % (name,age,pro,hobby))
#
# #也可以通过 f“内容{变量/表达式}” f-formatted
# name = "zsy"
# print(f"大家好,我是{name}")