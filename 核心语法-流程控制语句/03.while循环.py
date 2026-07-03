#while 条件表达式（bool值）：
#      循环体语句
#      ...
#也可以在后面加上一个else 执行条件为false的情况 可有可无
# step = 10
# while step > 0:
#     print(f"第{11-step}次说：人生苦短，及时行乐！")
#     step -= 1
# print("行乐去吧")

step = 2
total = 0
while step <= 100:
    total += step
    step += 2
print(total)