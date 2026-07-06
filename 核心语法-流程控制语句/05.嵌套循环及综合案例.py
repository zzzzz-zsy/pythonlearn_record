# #根据输入的长宽 打印由*号组成的矩阵
# row = int(input("请输入行数："))
# col = int(input("请输入列数："))
# #shift + enter 快速创建新行 无视光标位置
# for i in range(row):
#     for j in range(col):
#         print("* ",end=" ") #end改变末尾结束字符 默认换行
#     print()

# #案例：打印九九乘法表
# m = 9  # 任意阶乘法表
# for n in range(1,m+1): #外层控制行
#     for j in range(1,n+1): #内层控制列
#         print(f"{j} x {n} = {n*j} ", end="\t")
#     print()
#
# # #需求1：根据输入的直角边边长 打印等腰直角三角形（*）号组成
# num_side = int(input("请输入等腰直角三角形的直角边边长："))
# for n in range(1,num_side+1):
#     for j in range(1,n+1):
#         print("*", end="\t")
#     print()
#
# #需求2：根据输入的数字，打印对应的金字塔
# num = int(input("请输入边长数字："))
# for n in range(1,num+1):
#     for j in range(1,n+1):
#         print(j, end="\t")
#     print()
#
# #需求3：打印国际象棋棋盘
# num = 4
# for n in range(1,num+1):
#     for j in range(1,num+1):
#         print("■\t□", end="\t")
#     print()
#     for i in range(1,num+1):
#         print("□\t■",end="\t")
#         # print()
#     print()

#需求:根据输入的用户名密码执行登录操作,具体要求如下:
# 1.正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666
# 2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
# 3.输入的用户名和密码不能为空!
# 4.登录成功:输出"登录成功，进入B站首页~"
# 5.登录失败:输出"用户名或密码错误，请重新输入!"

#break :结束 跳出循环
#continue :中断本次循环 执行下一次循环
# while True:
#     #1.接收输入的用户名
#     username = input("请输入正确的用户名:")
#     password = input("请输入正确的密码:")
#
#     #校验:输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空!请重新输入")
#     #     continue
#     else:
#         match username :
#             case "admin":
#                 if password == "666888":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print("用户名或密码错误，请重新输入!")
#             case "zhangsan":
#                 if password == "123456":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print("用户名或密码错误，请重新输入!")
#             case "taoge":
#                 if password == "666888":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print("用户名或密码错误，请重新输入!")
#             case _:
#                 print("用户名或密码错误，请重新输入!")
#     #判断用户名和密码的正确性

# #练习:根据输入的用户名密码执行登录操作,具体要求如下:
# # 正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666 5次登陆机会 输入错误五次 不允许再次操作
# num_try = 1
# while num_try <= 5:
#     #1.接收输入的用户名
#     username = input("请输入正确的用户名:")
#     password = input("请输入正确的密码:")
#     # num_try += 1
#     if num_try == 5:
#         print("尝试次数已达最大,请联系管理员")
#         break
#     #校验:输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print(f"输入的用户名和密码不能为空!剩余{5-num_try}次机会，请重新输入")
#         num_try += 1
#     #     continue
#     else:
#         match username :
#             case "admin":
#                 if password == "666888":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print(f"用户名或密码错误，剩余{5-num_try}次机会，请重新输入!")
#                     num_try += 1
#             case "zhangsan":
#                 if password == "123456":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print(f"用户名或密码错误，剩余{5-num_try}次机会，请重新输入!")
#                     num_try += 1
#             case "taoge":
#                 if password == "666888":
#                     print("登录成功，进入B站首页~")
#                     break
#                 else:
#                     print(f"用户名或密码错误，剩余{5-num_try}次机会，请重新输入!")
#                     num_try += 1
#             case _:
#                 print(f"用户名或密码错误，剩余{5-num_try}次机会，请重新输入!")
#                 num_try += 1

#猜数字游戏
#使用函数 random 要先import
# 2.用户根据提示猜数字，并将所猜的数字输入系统
# 3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4.如果猜对，系统自动退出，游戏结束

import random
random_number = random.randint(1,100) #生成随机数

num = int(input("请输入一个数字:"))

while num != random_number:
     if num > random_number:
         # print("您输入的数字太大了!")
         num = int(input("您输入的数字太大了!请重新输入数字:"))
     else:
         num = int(input("您输入的数字太小了!请重新输入数字:"))
print("恭喜您,猜对了!")
print(f"生成的随机数是:{random_number}")
