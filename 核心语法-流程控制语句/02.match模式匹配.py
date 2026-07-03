# #结构模式匹配就是用一个清晰的 模板 去精准的匹配数据的结构和内容，匹配成果则执行相应的操作 match... case (_)匹配所有情况
#
# day = input("请输入星期几（1-7）：")
#
# match day:
#     case "1":
#         print("Mondy")
#     case "2":
#         print("Tuesday")
#     case "3":
#         print("Wednesday")
#     case "4":
#         print("Thursday")
#     case "5":
#         print("Friday")
#     case "6" | "7":
#         print("Sleeping")
#     case _:
#         print("Invalid input")
from unittest import case

# #简易计算器 实现一个计算器 可以实现 加减乘除运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算
# num_1 = float(input("请输入第一个数："))
# num_2 = float(input("请输入第二个数："))
# operator = input("请输入运算符：")
#
# match operator:
#     case "+":
#         print(f"{num_1}+{num_2} = {num_1 + num_2}")
#     case "-":
#         print(f"{num_1}-{num_2} = {num_1 - num_2}")
#     case "*":
#         print(f"{num_1}*{num_2} = {num_1 * num_2}")
#     case "/" if num_2 != 0:
#         print(f"{num_1}/{num_2} = {num_1 / num_2}")
#     case "//" if num_2 != 0:
#         print(f"{num_1}//{num_2} = {num_1 // num_2}")
#     case "^":
#         print(f"{num_1}^{num_2} = {num_1 ** num_2}")
#     case "%" if num_2 != 0:
#         print(f"{num_1}%{num_2} = {num_1 % num_2}")
#     case _:
#         print("操作不支持")

#练习：编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行想i用的动作（输出控制台）
operat = input("请输入角色移动指令：")

match operat:
    case "上" | "w" | "W":
        print("向上移动")
    case "下" | "s" | "S":
        print("向下移动")
    case "左" | "a" | "A":
        print("向左移动")
    case "右" | "d" | "D":
        print("向右移动")
    case "跳" | " ":
        print("跳跃")
    case "攻击" | "j" | "J":
        print("发动攻击")
    case "退出" | "esc" | "Esc":
        print("退出游戏")
    case _:
        print("error")
