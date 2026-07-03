# for 本质是一种轮询遍历机制 对一批内容进行逐个处理
# for 元素 in 待处理数据集:
#     循环体代码（对元素进行处理）
# else:  （可选）
    # 循环结束时，执行的代码

#案例 遍历字符串
# msg = "Hello-Python"
# #遍历字符串
# for i in msg:
#     print(i)
# else :
#     print("Hello-Python")

# msg = input("请输入需要遍历的字符串：")
# for c in msg:
#     print(c)
# print(msg)
# range range(end) 获取一个从0开始到end结束的数字序列 不包含end本身
# range（start，end）获取一个从start开始 到end结束的数字序列不含end本身
# range（start，end，step） 获取一个从start开始，到end结束的数字序列，step步长（不含end本身）

# 案例：基于for 完成计算100-500之间所有3的倍数之和
total = 0
for num in range(100,501):
    if num % 3 == 0:
        total += num
    num += 1;
print("100-500之间所有3的倍数之和:",total)