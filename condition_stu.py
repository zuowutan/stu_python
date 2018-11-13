#!/usr/bin/python
# coding=utf-8




# Python 的条件语句 if else 学习：
# a = 6
# if a > 10:
#     print "a大于10"
# else:
#     print "a小于10"
# # ---------------------------------------------------------
#
# # Python 的多重条件语句 if elif elif ... else 学习：
# if a > 2:
#     print "a大于2"
# elif a < 9:
#     print "a小于9"
# elif a > 7:
#     print "a大于7"
# elif a > 9:
#     print "a大于9"
# elif a > 11:
#     print "a大于11"
# else:
#     print "a..."
#
# # ---------------------------------------------------------
# # - or （逻辑或）：表示两个条件有一个成立（只需要一个为true）时，整个判断条件成功；
# # - and（逻辑与）：表示只有两个条件同时成立（同时为true）的情况下，整个判断条件才成功。
# data = 5
# if data >= 0 and data <= 10:  # 判断值是否在0-10之间
#     print '数值在0-10之间'
# else:
#     print "不在0-10之间"
#
# data = 10
# if data < 20 or data > 5:  # 判断值是否在小于20或大于5
#     print '数值小于20或数值大于5'
# else:
#     print '数值不在范围之内'
#
# data = 8
# # 判断值是否在0~5或者10~15之间
# if (data >= 0 and data <= 5) or (data >= 10 and data <= 15):
#     print '数值在0~5或者10~15之间'
# else:
#     print '数值不在范围之内'

# # ---------------------------------------------------------

# 解决Python复合布尔表达式中的一些问题：
a = 0
b = 1
# 这里把 **and**换成**or**程序就会报错

if a!=0 and b/a > 2:
    h = True
else:
    h = False

g = a > 0
if g or h:
    print "符合条件"
else:
    print "不符合条件"
# if (a > 0) or (b / a > 2):
#     print "符合条件"
# else:
#     print "不符合条件"




