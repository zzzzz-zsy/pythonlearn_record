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

#案例1，将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和 平均值。
num_list = []

for i in range(10):
    num_list.append( int(input("请输入一个数字:")))
print("数字列表:",num_list)

num_list.sort()

print("最大值:",num_list[-1])
print("最小值:",num_list[0]) #或者用 min() max()
#sum:求和 len:求长度
print("平均值:",sum(num_list)/len(num_list))

#案例2:合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)




