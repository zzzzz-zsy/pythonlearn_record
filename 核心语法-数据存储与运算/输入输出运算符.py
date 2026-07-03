#输入与输出
# input 输入 返回的数据类型是字符串
# print 输出
# name = input("请输入您的名字：")
# print(f"欢迎您，{name}")
# age = input("请输入您的年龄：")
# print(f"好的，您的名字是{name}，年龄是{age}")

# #模拟银行卡取款 -升级
# num_left = 10000 #银行卡余额
# num_password = 3 #银行卡密码输入尝试次数
# take_flag = True #取款标志
# input_password = input(f"请输入您的银行卡密码：")
# num_password = num_password -1
# while  take_flag :
#     if input_password == "123456":
#         print(f"您的银行卡余额为：{num_left}元")
#         num_take = input(f"请输入取款金额：")
#         num_left_temp = num_left - int(num_take)
#         if num_left_temp < 0:
#             take_flag = False
#             print("您的银行卡余额不足")
#             take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
#             # print(take_flag)
#         else:
#             num_left = num_left_temp
#             print(f"本次取款{num_take}元，您的剩余金额为{num_left}")
#             take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
#     else:
#         input_password = input(f"密码错误，请重新输入（剩余{num_password}次机会）:")
#         num_password = num_password -1
#         if num_password == 0:
#             take_flag = False
# if num_password == 0 :
#     print("今日密码错误次数过多，请明天尝试，或联系工作人员！")
# else:
#     print("感谢您的使用，欢迎下次光临~")
# # take_flag = True
# # take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
# # print(take_flag)

# 练习 根据用户输入的两个数字，计算两个数之和，并将其输出到控制台
# num_1 = input("本程序用简单求和，请输入第一个数：")
# num_2 = input("本程序用简单求和，请输入第二个数：")
# print(f"两数之和为：{int(num_1)+int(num_2)}")


# 运算符：
# 算术运算符：加（+） 减（-） 乘（*） 除（/，除法结果为小数） 整除（//，整除结果为整数，10//3=3） 取余/求模（%，10%3=1） 幂指数（**，4**2=16）
# print("10+4=",10+4)
# print("10-4=",10-4)
# print("10*4=",10*4)
# print("10/4=",10/4)
# print("10//4=",10//4)
# print("10%4=",10%4)
# print("10**4=",10**4)

#算数运算符优先级：** --> * / // % --> + -
# print("0.1 + 10 / 4**2 = ",0.1 + 10 / 4**2)
#案例 要求输入两个数x与y，分别输出x+y的结果和x-y的结果
# x = float(input("请输入x："))
# y = float(input("请输入y："))
# # float 会出现精度损失
# print("x + y = ",x+y)
# print("x - y = ",x-y)


# 赋值运算符：赋值（=） 加法赋值（+=） 减法赋值（-=） 乘法赋值（*=） 除法赋值（/=） 取余赋值（%=） 取整除赋值（//=） 幂赋值（**=）
# num += 2 --> num = num + 2
# num *= 2 --> num = num * 2
# num **= 2 --> num = num ** 2
# num //= 2 --> num = num // 2
# num = 10
# num *= 2
# print("num *= 2 后：",num)
# num /= 3
# print("num /= 3 后：",num)
# num //= 3
# print("num //= 3 后:",num)



# 比较运算符（返回布尔值 True False）： 等于（==） 不等于（！=） 大于（>） 大于等于（>=） 小于（<） 小于等于（<=）

# print(10 == 10,10 != 10,10 > 10,10 < 10)

# 逻辑运算符（返回布尔值 True False）：与（and） 或（or）  非（not）
# print(10 < 10 and 10 < 20)
# print(10 > 10 and 10 > 20)
# print(10 > 10 or 10 < 20)
# print(not 10 < 20)
# 
# num = float(input("请输入一个数："))
# print(num > 10 and num < 20)
# print(num < 10 or num > 20)
