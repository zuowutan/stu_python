#!/usr/bin/python
# coding=utf-8


#字典的定义

# 使用前就定义字典
endDict = {'name': 'tom', 'code': "Python", 'profession': 'Coder'}
# 输出完整的字典  {'code': 'Python', 'profession': 'Coder', 'name': 'tom'}
print endDict

# 输出所有键  ['code', 'profession', 'name']
print endDict.keys()

# 输出code键 找到对应的value  Python
print endDict['code']

# 输出所有属性值  ['Python', 'Coder', 'tom']
print endDict.values()




dictData = { }
dictData['key1'] = "key1 对应的属性值"
dictData[2] = "2对应的属性值"
dictData[3] = True
dictData['hello'] = "我爱你中国"
dictData['word'] = 520.1314

print dictData['hello']          # 输出键为'hello' 的值    我爱你中国
print dictData['word']           # 输出键为 word 的值   520.1314



#字典的定义
print ("---------字典-------------")




#元组的定义
print ("---------元组-------------")
tupleData = (True, "False", 520, 13.14)
smallTupleData = (456, 'Tom')
# 元组不支持设置 属性值 否则会报错  TypeError: 'tuple' object does not support item assignment

print tupleData[0]

# 输出完整元组  (True, 'False', 520, 13.14)
print tupleData

# 输出元组的第一个元素  True
print tupleData[0]

# 输出第二个至第三个的元素  ('False', 520)
print tupleData[1:3]

# 输出从第三个开始至列表末尾的所有元素  (520, 13.14)
print tupleData[2:]

# 输出元组两次  (True, 'False', 520, 13.14, True, 'False', 520, 13.14)
print tupleData * 2

# 打印组合的元组  (True, 'False', 520, 13.14, 456, 'Tom')
print tupleData + smallTupleData

print ("---------元组-------------")

#列表的定义
listData = [True, "False", 233, 12.3]
smallListData = [123, 'john']

# 输出完整列表   [True, 'False', 233, 12.3]
print listData

# 输出列表的第一个元素  True
print listData[0]

# 输出第二个至第三个元素 ['False', 233]
print listData[1:3]

# 输出从第三个开始至列表末尾的所有元素  [233, 12.3]
print listData[2:]

# 输出列表两次  [123, 'john', 123, 'john']
print smallListData * 2

# 打印组合的列表  [True, 'False', 233, 12.3, 123, 'john']
print listData + smallListData

# ---------List-------------



# ---------字符串-------------
a = 'Hello World!'
# 完整字符串  输出：Hello World!
print a

# 输出字符串中的第一个字符  输出：H
# 这个大家不陌生，字符串根据索引输出对应的属性值
print a[0]

# 输出字符串中第三个至第五个之间的字符串   输出：llo
print a[2:5]

# 输出从第三个字符开始的字符串   输出：llo World!
print a[2:]

# 输出字符串两次   输出：Hello World!Hello World!
print a * 3

# 输出连接的字符串   输出：Hello World! Python
print a + " Python"
