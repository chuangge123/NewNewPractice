# 变量：存储信息的，日后被调用，修改操作。
# 常亮：固定不变的量，字母大写
# 命名规则：
# 1.字母数字下划线组成
# 2.不能以数字开头，不能含有特殊字符和空格
# 3.不能以保留字命名
# 4.不能以汉字命名
# 5.定义的变量名应该有意义
# 6.驼峰式命，下划线分割单词
# 7.变量区分大小写

# 单行注释
"""
  多行注释
"""

"""
一.and or not 逻辑运算符的规则
条件1 and 条件2
条件1 or  条件2
and or not 优先级是一样的
但是有短路原则
对于and如果前面的条件1为假 则不去计算条件2
对于or 如果前面的条件1位真 则不去计算条件2
举例：
not not True or False and not True
因为前面为真  所以or后面的不去计算
输出结果为 TRUE

"""
"""
二 循环语句
while 条件：
    执行1
    执行2
举例：输出1——100中的偶数，初始num=1;
解决代码如下：
num = 1
while num<=100:
    if num%2 ==0:
        print(num)
    num +=1
"""
# 猜年龄小游戏
# age = 50
# flag = True
# while flag:
#     user_input_age = int(input("Age is:"))
#     if user_input_age == age:
#         print("yes")
#         flag = False
#     elif user_input_age > age:
#         print('猜测年龄大了')
#     else:
#         print("猜测年龄小了")
"""
  以上代码也可以把 flag 标 替换成 break也能完成程序。
  continue 代表的是跳过这一项  比如在 if num = 3:  continue 那么就是这一项在num=3时 不去执行。
"""
"""
  while else 语句 是在执行完while 语句后 （不是break 跳出循环的）则会继续执行 else语句中的代码。
  下面执行一个小程序，运行就一目了然了
"""
# num = 0
# while num < 10:
#     num += 1
#     if num == 3:
#         continue
#     print(num,end=" ")
# else:
#     print('执行了while else statement')
"""
  插曲，如何将分单行输出的语句 变为一行呢 ，只需要在print后面加一个end=""
"""
# 输入长宽给画图
# print('请输入长')
# length = int(input())
# print('请输入宽')
# wide = int(input())
# num1 = 0
# while num1 < length:
#     num2 = 0
#     while num2 < wide:
#         print('#', end='')
#         num2 += 1
#     print()
#     num1 += 1


# *
# **
# ***
# ****   输出这样
# print('输入期望几行几列')
# EC = int(input())
# lie = 0
# while lie < EC:
#     hang = 0
#     while hang < lie + 1:
#         print('*', end="")
#         hang += 1
#     lie += 1
#     print()

# 输出九九乘法表
# hang = 1
# while hang <= 9:
#     lie = 1
#     while lie < hang + 1:
#         print(str(lie) + "*" + str(hang) + "="+str(lie*hang), end=" ")
#         lie += 1
#     print()
#     hang += 1
