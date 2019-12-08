# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/12/8
"""
进程相关内容
"""
import os
from multiprocessing import Process  # 引入进程的包。
import time

# def f(name):
#     time.sleep(1)
#     print('hello进程以启动')
#     print(os.getpid())  # 获取当前进程 的号码
#     print(os.getppid())  # 获取父进程的号码 （这里是pycharm 的进程号） ,每一个子进程，都会有父进程
#
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):  # 这里 是开辟了三个子进程，在外加一个主进程，一共是有四个进程。
#         p = Process(target=f, args=('sun',))
#         p_list.append(p)
#         p.start()
#     for i in p_list:
#         i.join()
#     print('end')
#
#
# class MyProcess(Process):  # 第二种创建进程的方式
#     def __init__(self, name):  # name 是对进程的名字进行赋值
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     def run(slef):
#         time.sleep(1)
#         print('hello进程以启动', slef.name)
#
#
# if __name__ == '__main__':
#     p = MyProcess('sun')
#     p.start()
"""
进程之间的通信
    queue 管道
"""
# import os
# from multiprocessing import Process, Queue  # 引入进程的包。
# import time
#
#
# def f(q):
#     q.put(['hello'])
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p_list = []
#     for i in range(3):
#         p = Process(target=f, args=(q,))  # 需要让主进程 把这个管道当参数传过去 这里的args = 后面要有()
#         p_list.append(p)
#         p.start()
#     print(q.get())
#     print(q.get())
#     print(q.get())
"""
    Pipe 管道
    
"""
# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send('儿子')
#     conn.send('儿子')
#     print(conn.recv())
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())
#     print(parent_conn.recv())
#     parent_conn.send('我是你爹')
"""
    数据共享

"""
from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()