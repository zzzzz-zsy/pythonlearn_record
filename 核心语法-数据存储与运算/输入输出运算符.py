#输入与输出
# input 输入 返回的数据类型是字符串
# print 输出
# name = input("请输入您的名字：")
# print(f"欢迎您，{name}")
# age = input("请输入您的年龄：")
# print(f"好的，您的名字是{name}，年龄是{age}")

num_left = 10000
num_password = 2
take_flag = True
input_password = input(f"请输入您的银行卡密码：")
while  take_flag :
    if input_password == "123456":
        print(f"您的银行卡余额为：{num_left}元")
        num_take = input(f"请输入取款金额：")
        num_left_temp = num_left - int(num_take)
        if num_left_temp < 0:
            take_flag = False
            print("您的银行卡余额不足")
            take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
            # print(take_flag)
        else:
            num_left = num_left_temp
            print(f"本次取款{num_take}元，您的剩余金额为{num_left}")
            take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
    else:
        input_password = input(f"密码错误，请重新输入（剩余{num_password}次机会）:")
        num_password = num_password -1
        if num_password == 0:
            take_flag = False
if num_password == 0 :
    print("密码错误次数过多，请明天尝试，或联系工作人员！")
else:
    print("感谢您的使用，欢迎下次光临~")
# take_flag = True
# take_flag = (input("是否继续取款？（1：继续，2：退卡）") == '1')
# print(take_flag)