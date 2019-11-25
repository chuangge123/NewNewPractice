# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/18
"""
  多行注释
"""
"""
生成器
    1.列表生成式 a = [x*2 for x in range(10)] 生成一到九分别乘以2的这个列表
    #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    def f(n):
    return n**3
    a = [f(x) for x in range(10)] #0 1 8 27 ...列表生成器里可以放入函数。   
    
    2.（）创建 生成器
    s = (x*2 for x in range(100))
    print (s) 这是一个生成器对象,需要一个时候就next拿出来一个。
    print(next(s)) 
    生成器 就是一个可迭代对象。
    
    3.*yield 创建生成器 
    def foo():                     
        print('ok')
        count = yield 1
        print (count)
        print('ok2')
        yield 2
    g = foo()                       ok 1 ok 2
    a = next(g)         #一个yield 就是迭代一次 两个就迭代两次，继续next(）
    print(a)             每次next一个值，则会返回一个值，这里我们用变量去接收并分别打印。
    b = next(g)
    情况2.用send进行Yield
    b.send(None)      Send 就是为 yield前的变量传值，但是第一次send前如果没有next,只能传一个send(None)   ，因为此时要进入执行，并不知道传给谁
    ret = b.send("eee")  此时继续从上次yield 地方继续开始，而这个时候count ="eee",并继续往下执行。                            
    
"""
"""
迭代器
    生成器都是迭代器，迭代器不一定是生成器。
    List,tuple,dict,string: 都是可迭代对象Iterable()
    
    迭代器 都要有iter方法，和next 方法。
    for循环内部三件事
    1.调用可迭代对象的iter 方法，返回一个迭代器对象
    2.不断调用迭代器对象的next()方法
    3.处理StopIteration
    
    isinstance 括号里前面对象，后面是要确认的对象。 该函数是判断。。。是否是什么
    print (isinstance([1,2],list))
    l = [1,2,3,5]
    print(isinstance(l,Iterable)) 查看是不是迭代对象。
"""

# 斐波那契数列新算法
# def fib(Max):
#     n, before, after = 0, 0, 1
#     while n < Max:
#
#         yield before
#         before, after = after, before + after
#         n = n + 1
#
#
# fib(10)
