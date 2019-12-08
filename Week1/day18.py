# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/12/8
"""
携程
    一个线程，如果需要转换就转换。 效率高，
    缺点，用不上多核 ， 可以通过多进程+协程
    ，有一个阻塞  协程就会停止。
"""
"""
greenlet 模块
"""
# from greenlet import greenlet  # 支持用yield 做协程的库
#
#
# def test1():
#     print('one the first')
#     gr2.switch()
#     print('this is two')
#     gr2.switch()
#
#
# def test2():
#     print('two two one')
#     gr1.switch()
#     print('two,two ,two')
#
#
# gr1 = greenlet(test1)   #类似生成一个生成器对象。
# gr2 = greenlet(test2)
# gr1.switch()  #switch 有点类似于next
"""
gevent 模块   遇到阻塞会自动切换到别的
"""
import gevent


def foo():
    print('11')
    gevent.sleep(0) #模拟io 阻塞
    print('222')


def bar():
    print('33')
    gevent.sleep(0)
    print('4444')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
