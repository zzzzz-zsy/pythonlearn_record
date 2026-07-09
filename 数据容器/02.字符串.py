#基本操作
#字符串:字符的容器,一个字符串可以存放任意数量的字符 s = 'hello' "hello" """hello"""
# 特点:不可变性(无法修改) 有序性 可迭代性
# 字符串中的每一个字符都有其对应的下标 与列表类似,也可以正反向索引(正向0开始 反向-1开始)
# 字符串也可以进行切片操作:序列对象[开始:结束:步长]不包含结束索引位置对应的位置
# s = 'hello-python'
#
# print(s)
# print(s[0:-1])
# print(s[::-1]) #逆序输出

#字符串常用方法:
# find() 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1 s.find('Python')
# count() 统计子串在字符串中出现的次数  s.count('H')
# upper() 将字符串中的所有字母转换为大写 s.upper() 返回新字符串
# lower() 将字符串中的所有字母转换为小写  s.lower() 返回新字符串
# split() 将字符串按指定分隔符分割成列表 s.split(' ') 返回新字符串
# strip() 去除字符串两端的空白字符或指定字符 s.strip() / s.strip('*') 返回新字符串
# replace() 将字符串中的指定子串替换为新的子串  s.replace('H','c') 返回新字符串
# startswith() 检查字符串是否以指定子串开头，返回布尔值 s.startwith('P') 与之对应的endwith
# s = 'hello-python-HELLO-PYTHON'
# print(s.find('Python'))
# print(s.count('H'))
# print(s.upper())
# print(s.lower())
# print(s.replace('python','Java'))
# print(s.startswith('h'))
# print(s.endswith('Python'))
# print(s.split('-'))
# print(s) #字符串不变


# #案例:邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。
# # 方式一:
# mail_address = input("请输入邮箱:")
#
# if mail_address.count("@") == 1 and mail_address.count('.') >= 1:
#     print(f"{mail_address}格式正确")
# else:
#     print(f"{mail_address}格式错误")
# # 方式二:
# mail_address = input("请输入邮箱:")
# if mail_address.count("@") == 1 and '.' in mail_address:
#     print(f"{mail_address}格式正确")
# else:
#     print(f"{mail_address}格式错误")

# # 练习 1.输入一个字符串，判断该字符串是否是回文(两边对称)
# # 黄山落叶松叶落山黄
# # 上海自来水来自海上
# string = input("请输入语句:")
#
# back = string[::-1]
# if back == string:
#     print("输入的语句是回文的")
# else:
#     print("输入的语句不是回文的")


#练习2:将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
string = input("请输入十个字符串,以空格隔开:")
print(f"您输入的字符串为:{string}")

string_list_temp = string[::-1]
string_list_temp = string_list_temp.upper()
string_list = string_list_temp.split(' ')
for i in range(len(string_list)):
    print(string_list[i])
