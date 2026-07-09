# #列表是数据容器的一类,是一次性可以存储多个元素的
# #定义: 列表名称 = [元素1,元素2,元素3,.....]元素之间逗号隔开
# #特点:可以存储不同类型的元素,元素有序(从0开始索引) 可以重复 可以修改
# #也可以反向索引(-1表示最后一个,往前索引) 比如s = [25,25,63,45,36,85] s[0] = s[-6] = 85
# s = [25,65,63,45,36,85,"A","hello"]
#
# #获取
# print(type(s))
# print(s[0]) #25
# print(s[-1]) #63
#
# #修改
# s[3] = 125
# print(s)
#
# #删除 使用关键字 del
# del s[3]
# print(s)
# for item in s:
#     print(item,end=" ")

#list 切片:对操作的数据截取其中一部分的操作.列表 字符串 元组都支持切片操作
#序列数据[开始索引:结束索引:步长] 包含开始索引,不包含结束索引 开始索引未指定默认为0;结束索引未指定默认为列表长度(直到列表末尾),步长未指定默认为1
#索引采用正方向都可以
#切片出来的也是list类型
# s = ["l","i","a","o","x","i","l","u","n","廖希伦"]
#
# #切片操作:
# print(s[0:5:1])
# print(s[0:5:2])
# print(s[0:5:3])
# print(s[0:-5:1])

#方法:物品具备的能力或功能 方法属于对象
#列表内置功能
# 方法
# append() 在列表的尾部追加元素 s.append (10086)
# insert() 在指定索引之前，插入该元素 s.insert(0, 92)
# remove() 移除列表中第一个匹配到的值 s.remove(75)
# pop() 删除列表中指定索引位置的元素(如果未指定索引，默认删最后一个) s.pop(2)/ s.pop()
# sort() 对列表进行排序(列表元素的数据类型一致，才可以进行排序) s.sort()
# reverse() 反转列表元素 s.reverse()

# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
#
# s.append(188)
# print(s)
#
# s.insert(2,80)
# print(s)
#
# s.remove(90)
# print(s)
#
# s.pop(2)
# print(s)
#
# s.sort()
# print(s)
#
# s.reverse()
# print(s)
#
# s_copy = s.copy()
# print(s_copy)
#
# print(s.count(100))

# #案例1，将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和 平均值。
# num_list = []
#
# for i in range(10):
#     num_list.append( int(input("请输入一个数字:")))
# print("数字列表:",num_list)
#
# num_list.sort()
#
# print("最大值:",num_list[-1])
# print("最小值:",num_list[0]) #或者用 min() max()
# #sum:求和 len:求长度
# print("平均值:",sum(num_list)/len(num_list))

# #案例2:合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# #合并列表
# for num in num_list2:
#     # if num not in num_list1:
#         num_list1.append(num)
#
# print(num_list1)
# #去重处理
# new_list = []
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

# #案例2(简化):合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# #合并列表
# # new_list1 = num_list1 + num_list2
# # new_list1 = [*num_list1 , *num_list2] #解包然后再组包
# new_list1 = [num_list1 ,num_list2]
# print(new_list1)
# #去重处理
# new_list = []
# for num in new_list1:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

# #案例2:生成1-20的平方列表
# #方法一:
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
#
# #方法二:列表推导式
# num_list = [i**2 for i in range(1,21)]
# print(num_list)

# #案例4:从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
# num_list = [12,25,36,69,65,54,47,58,69,25,14,32,36]
# new_list = [i**2 for i in num_list if i%2== 0 ]
# print(new_list)

#列表推导式
# 用途：快速生成列表。
# 语法：[返回值 for 元素 in 可迭代对象 if 条件]
# 返回值：返回一个新的列表

##练习
# #练习1:将如下多个列表合并为一个列表，并去重重复元素，排好序(升序)后输出到控制台。
# #合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
# # list2=['X','Z','T','Y','D','E','F','G']
# # list1 = ['M','A','C','E','F','G','H','L',N','I','J','K','O']
# # list3 = ['w','A','S','D']
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
# new_list1 = list1 + list2 + list3
# new_list = []
# for num in new_list1:
#     if num not in new_list:
#         new_list.append(num)
# new_list.sort()
# print(new_list)

#练习2:
#将如下列表中能被3 或5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 30]
# new_list = [i**2 for i in list1 if i%2==0 or i%5==0]
# print(new_list)

# #练习3:将如下列表中的正数提取出来，封装为一个新的列表。
# #list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = [i for i in list1 if i > 0]
# print(new_list)