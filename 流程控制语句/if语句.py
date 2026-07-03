# 判断语句if bool值 :
# score = float(input("请输入分数："))
# if score >= 680:
#     print("欢迎报考清华大学！")
# print("_________________")

#模拟b站账号登陆
#账号：18888888888 密码666888
# ok_ID = 18888888888
# ok_password = 666888
# num_ID = int(input("请输入账号:"))
# num_password = int(input("请输入密码："))
# if num_ID == ok_ID:
#     if num_password == ok_password:
#         print("登陆成功")
#     else:
#         print("密码错误！")
# else:
#     print("账号输入错误")

#案例 根据用户输入的年份，判断这一年是闰年还是平年
# 非整百年份，且能被4整除的年份是闰年
# 整百年份必须能被400整除才是闰年
year = int(input("请输入需要判断的年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")