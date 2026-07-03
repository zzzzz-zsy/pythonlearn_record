# #根据输入的长宽 打印由*号组成的矩阵
# row = int(input("请输入行数："))
# col = int(input("请输入列数："))
# #shift + enter 快速创建新行 无视光标位置
# for i in range(row):
#     for j in range(col):
#         print("* ",end=" ") #end改变末尾结束字符 默认换行
#     print()

# #案例：打印九九乘法表
m = 9  # 任意阶乘法表
for n in range(1,m+1): #外层控制行
    for j in range(1,n+1): #内层控制列
        print(f"{j} x {n} = {n*j} ", end="\t")
    print()

# #需求1：根据输入的直角边边长 打印等腰直角三角形（*）号组成
num_side = int(input("请输入等腰直角三角形的直角边边长："))
for n in range(1,num_side+1):
    for j in range(1,n+1):
        print("*", end="\t")
    print()

#需求2：根据输入的数字，打印对应的金字塔
num = int(input("请输入边长数字："))
for n in range(1,num+1):
    for j in range(1,n+1):
        print(j, end="\t")
    print()

#需求3：打印国际象棋棋盘
num = 4
for n in range(1,num+1):
    for j in range(1,num+1):
        print("■\t□", end="\t")
    print()
    for i in range(1,num+1):
        print("□\t■",end="\t")
        # print()
    print()