# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/14
"""
  多行注释
"""
"""
函数
    调用方式为 函数名（）
    1.参数分为，形参和实参。
    add(a,b) 默认的和实参是一一对应的（无命名参数） hobby ='sdf' 有名字的参数（键值对）
    add(*args） 会把所有无命名参数变为一个元组。
    add(**args)    会把命名的参数 放入字典 
    位置关系 无名字在左 ，有名字要在右。
    关键参数 ， 默认参数，（name  age=0  *args  **args）
    2. 如果return 多个对象，python 会把这多个对象，封装成一个元组 返回。
    3.高阶函数
    def f(n):
    return n * n
    def foo(a, b, fun):
        return fun(a) + fun(b)
    print(foo(1, 2, f)) 就是把函数名，当成实参来传递给另一个函数。
    函数的名字 可以是参数，也可以作为返回值。
    那么在return 函数名字的时候，返回的是一个地址。
递归函数
    函数自己调用自己 完成阶乘，2.要有结束，3.所有递归能做的循环都能完成。 4.递归效率低
    def fact(n):
        if n==1:
            return 1
    
        return  n*fact(n-1)
    res = fact(5)
    print(res)
内置函数
    自己需要了解。
闭包
    定义：如果在一个内部函数里，对在外部作用于的变量进行引用，那么内部函数就被认为是闭包。
    def outer():
        x=10
        def inner():
            print(x)
        :return inner 
    结论：存在闭包时，定义内部函数的环境皆可被内部函数调用。
"""


