#!/usr/bin/python
# coding=utf-8

#运算符的学习：
#Python算术运算符

a = 5
b = 2

x = a % b
# 返回除法的余数 3/2  取模余 1
# print "a % b 的值为：", x

y = a ** b
#等价于a的b 次方
# print "a ** b 的值为：", y

z = a // b
# 取整除 返回商的整数部分
# print "a // b 的值为：", z

# 所谓的比较运算符，就是比较a\b两个的关系(相等、大于、小于)，返回值是true或者false，常见的比较运算符有以下几种：
# - 大于运算符（使用符号：>）
# - 小于运算符（使用符号：<）
# - 相等运算符（使用符号：==）
# - 不等运算符（使用符号：<>）
# - 不等运算符（使用符号：!=）
# - 大于等于运算符（使用符号：>=）
# - 小于等于运算符（使用符号：<=）
#
# 其中，不等运算符有2种表现形式，一种是习惯的用**!=**来表达不等运算符，还有一种是使用<>，这个是要值得注意的，代码如下：

# a = 5
# b = 2
# # - 大于运算符（使用符号：>）
# print "a > b == ", a > b
#
# # - 小于运算符（使用符号：<）
# print "a < b == ", a < b
#
# # - 相等运算符（使用符号：==）
# print "a < b == ", a == b
# # - 不等运算符（使用符号：<>）
# print "a <> b == ", a <> b
#
# # - 不等运算符（使用符号：!=）
# print "a != b == ", a != b
#
# # - 大于等于运算符（使用符号：>=）
# print "a >= b == ", a >= b
#
# # - 小于等于运算符（使用符号：<=）
# print "a <= b == ", a <= b

# Python赋值运算符：
a = 2
b = 3
c = 4
# - 直接赋值运算符（使用符号：=）如：c = a + b ，就是将 a + b 的结果赋值给 c
# print "c = ", a + b
#
# # - 加法赋值运算符（使用符号：+=）如：c += a 等价于 c = c + a
# print "c += a = ", c + a
#
# # - 减法赋值运算符（使用符号：-=）如：c -= a 等价于 c = c - a
# print "c -= a = ", c - a
#
# # - 乘法赋值运算符（使用符号：*=）如：c *= a 等价于 c = c * a
# print "c *= a = ", c * a
#
# # - 除法赋值运算符（使用符号：/=）如：c /= a 等价于 c = c / a
# print "c /= a = ", c / a
#
# # - 取模赋值运算符（使用符号：%=）如：c %= a 等价于 c = c % a
# print "c %= a = ", c % a
#
# # - 幂赋值运算符（使用符号：**=）如：c ** a 等价于 c = c 的 a 次方
# print "c ** a = ", c ** a
#
# # - 取整除赋值运算符（使用符号：//=）如：c //= a 等效于 c = c // a
# print "c // a = ", c // a


# Python的成员运算符
# a = 2
# b = 6
# listData = [1, 2, 3, 4, 5]
# if( a in listData ):
#     print "in语句 - a在该范围之内"
# else:
#     print "in语句 - a不在该范围之内"
#
# if( b in listData ):
#     print "in语句 - b在该范围之内"
# else:
#     print "in语句 - b不在该范围之内"
#
# if( a not in listData ):
#     print "not in语句 - a不在该范围之内"
# else:
#     print "not in语句 - a在该范围之内"
#
# if( b not in listData ):
#     print "not in语句 - b不在该范围之内"
# else:
#     print "not in语句 - b在该范围之内"


# # Python的身份运算符
# a = 45414121
# b = 45414121
# if( a is b ):
#     print "is语句 - a true b"
#     print "is语句 - a 在内存中的地址",id(a)
#     print "is语句 - b 在内存中的地址",id(b)
# else:
#     print "is语句 - a false b"
#
# if( a is not b ):
#     print "is not语句 - a和b不是同一个引用"
# else:
#     print "is not语句 - a和b是同一个引用"


a = 2.0
b = 3.0
c = 4.0
d = 5.0

e = (a + b) * c / d
print "(a + b) * c / d 运算结果为：", e

e = ((a + b) * c) / d
print "((a + b) * c) / d 运算结果为：", e

e = (a + b) * (c / d)
print "(a + b) * (c / d) 运算结果为：", e

e = a + (b * c) / d
print "a + (b * c) / d 运算结果为：", e

e = ( a**b + a ) / d
print "( a**b + a )/ d 运算结果为：", e

e =  a**b + c / a
print " a**b + c / a 运算结果为：", e


# # Python逻辑运算符
# a = 2
# b = 3
# c = "Python"
#
# if a and c:
#     print " test and - 变量 a 和 b 都为 true"
# else:
#     print " test and - 变量 a 和 b 有一个不为 true"
#
# if c or a:
#     print "test or - 变量 a 和 b 都为 true，或其中一个变量为 true"
# else:
#     print "test or - 变量 a 和 b 都不为 true"
