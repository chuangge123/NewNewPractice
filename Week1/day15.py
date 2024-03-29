# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/29
"""
sever 端
socket
    socket 网络编程
    sk = socket.socket()
            family = AF_INET           IPV4环境下 服务器之间的通信  AF_INET6   IPV6环境下
            familu = AF_UNIX           Unix 不同进程之间得数据通讯
            type = SOCK_STREAM         TCP 协议下 数据流传输数据
            type = SOCK_Dgram          UDP 用的 报文传输数据

    address = ('127.0.0.1',8000)
    sk.bind(address)            绑定ip 和 端口
    sk.listen(3)                是准许最大连接数，最大连接数内的线程准许等待着。 其他线程在想连就会报错。
    conn = sk.accept()          阻塞住 等待其他线程来访问，无人访问，就这么等着
    recv()      收信息
    send()      发信息             发送的内容一定要是bytes类型
    sendall()   循环发送所有        发    coon.send(bytes(发送内容,'utf8')) 当发送为字符串时，由于只能发送bytes格式，所以需要转下
                                   收       data = coon.recv(1024) 即为一次最大收多少
                                            不得超过8k,多的话需要获取接受内容的大小，并分阶段传递给个变量。
                                   注：server client 端的 sk 只是为了等待进程访问用的  但是发送一定要用 coon发送。
                                   转码 print (str(data,'utf8'))
    coon.close  是关闭通道
    sk.close    是关闭服务
"""

"""
client 客户端
import socket
    sc = socket.socket()
    address = ('127.0.0.1',8000)
    coon = sk.connect()     链接                 发送需要用 coon.send()
    recv()      收信息                 收       data = sk.recv(1024) 即为一次最大收多少
    send()      发信息             
    sendall()   循环发送所有    发送的内容一定要是bytes类型    
    sk.close()
"""

"""
执行shell语句
import subprocess
data = 'java'
obj = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)    subprocess.PIPE是通过管道由子进程转移到主进程
cmd_result = obj.stdout.read()  获取来的东西本身就是bytes数据类型。
"""
# 代码实例
# import subprocess
#
# data = 'java'
# obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
# cmd_result = obj.stdout.read()
# cmd_len = bytes(str(len(cmd_result)),'utf8')
# print(cmd_len)
# conn.sendall(cmd_len)
# conn.sendall(cmd_result)
"""
以上代码 涉及一个粘包现象
当第一个send 发送的字节特别小时，那么cpu会等待一下，会把第二send一起发送过去。但是随即发生
正确的写法是 将他俩隔断开
用 conn.recv(1024) 来隔断 是正确的   确认那边收到了一个send 给传回来个值，就ok的解决了这个现象。
"""

# str(cmd_result,'utf8')
# print(str(cmd_result,'utf8'))
# 在用建立的 conn.sendall (cmd_result)


# cmd_client  做个循环来回接受已有参数。因为有的时候字节过大的名利不能一次全部接受完。
# result_len = int(str(sk.recv(1024),'utf8'))
# data = bytes()
# while len(data)!= result_len:
#     recv = sk.recv(1024)
#     data+=recv
#     print(str(data,'gbk'))

"""
编码
    py3: str  bytes    python3只有这两种数据类型。
    str: unicode     
    bytes: 十六进制数
    encode() 编码
    decode() 解码
    s.encode('utf8')方法一
    s ='hello 孙闯'
    b= bytes(s,'utf8')方法二  把字符串unicode，根据utf8规则 转为bytes 
    print(b)            b'hello \xe5\xad\x99\xe9\x97\xaf'
"""
"""
server 实现并发。
"""
# import socketserver
#
#
# # 想要并发 必须写个类 ，类要继承 这个
# class MyServer(socketserver.BaseRequestHandler):
#     # handle 方法源自于父类，在这里重写，名字不能更改。
#     def handle(self):
#         print('服务器已启动')
#         while True:
#             # 之前的接收逻辑需要写到这个方法里
#             # 先获取连接 通过这个方法
#
#             coon = self.request
#             print(self.client_address)
#             while True:
#                 client_data = coon.recv(1024)
#                 print(str(client_data, 'utf8'))
#                 print('waiting...')
#                 coon.sendall(client_data)
#             coon.close()
#
#
# if __name__ == '__main__':
#     # 调用这个方法 绑定端口  TCP协议用 TCPServer实现端口连接，从而完成多线程。
#     # 相当于 sc = socket.socket()
#     #     address = ('127.0.0.1',8000)   被封装了
#     server = socketserver.ThreadingTCPServer(('127.0.0.1', 8090), MyServer)
#     # 启动
#     server.serve_forever()
#     # 或者下面的方法
#     server.handle_request()
"""
线程的创建
    一个线程就是一堆指令集
    join 进行阻塞这样反而更快，是因为省去了线程来回切换的时间。
    python 解释器 有一个GIL 全局解释器锁（在同一时刻，只能有一个线程）这样对数据处理更安全方便
    解决思路，: 1.多进程可以调动多核（不完美）。2.协程
    综上: if 任务是IO密集类型的，python 还可以多线程 。如果不是就换语言吧。
    
"""
import threading
import time
from random import randint

#
# def foo(n):
#     time.sleep(1)
#     print('foo线程执行，并接收参数%s' % n)
#
#
# def bar(n):
#     time.sleep(2)
#     print('bar线程执行，并接受参数%s' % n)
#
#
# # args是目标调用的参数元组，默认为（）
# t1 = threading.Thread(target=foo, args=(1,))
# t2 = threading.Thread(target=bar, args=(2,))
# # 设置某个线程为守护线程  把谁设成守护线程，在主线程完成时，就不会继续等守护线程。
# t2.setDaemon(True)
# t1.setDaemon(True)
# t1.start()
# t2.start()
# # 阻塞一下，这个进程不完成，不准往下走。
# # t1.join()
# print('我是主线程')
# 三个主线程 不分先后的执行着
"""
r = threading.Lock()                r = threading.RLock() 通用锁。避免死锁。(递归锁)(锁2)
r.acquire() 获取锁
r.release() 释放锁
"""
"""
信号量(锁3)
    semaphore = threading.BoundedSemaphore(5)   相当于 有五个车位 ，并行的进行。
"""

# class myThread(threading.Thread):
#     def run(self):
#         if semaphore.acquire():
#             print(self.name)
#             time.sleep(3)
#             semaphore.release()
#
#
# if __name__ == '__main__':
#     semaphore = threading.BoundedSemaphore(5)
#     thrs = []
#     for i in range(100):
#         thrs.append(myThread())
#     for t in thrs:
#         t.start()
"""
条件变量(锁4) 涉及到生产者，消费者模型
    ifLock = threading.Condition()
    ifLock.notify()
    ifLock.wait()    实现了线程间的通信
"""
# 吃包子 做包子 小程序
# class Producer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             val = randint(0, 100)
#             print('生产者', self.name, ':Append' + str(val), L)
#             if lock_con.acquire():
#                 L.append(val)
#                 lock_con.notify()
#                 lock_con.release()
#             time.sleep(3)
#
#
# class Consumer(threading.Thread):
#     def run(self):
#         global L
#         while True:
#             lock_con.acquire()
#             if len(L) == 0:
#                 lock_con.wait()
#             print('消费者', self.name,'吃掉'+str(L[0]),L)
#             del L[0]
#             lock_con.release()
#             time.sleep(0.25)
#
#
# if __name__ == '__main__':
#     L = []
#     lock_con = threading.Condition()
#     threads = []
#     for i in range(5):
#         threads.append(Producer())
#     threads.append(Consumer())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
"""
同步条件(Event) 
    event.isSet():返回event内置标志位的状态值:
    event.wait(): 如果event.isSet()==False,就会阻塞线程:
    event.set():设置event的状态值为True.那么所有阻塞的线程都会被激活，准备处理。
    event.clear() 恢复event的状态为False.
"""
"""
队列:** queue 先进先出。
    t = queue.Queue(10) 这里不设参数 默认为0 0代表无限大
    t.put('aisi')
    t.put('lufei')
    t.put('shanzhi')
    print(t.get())
    列表内部是有锁的，不会有多个线程拿到同一个值的现象。
    
下面用列表 实现吃包子 就会发现代码真的很简单
如果 队列没有包子了，程序会自动进入阻塞， 如果列表中塞不下包子了，程序也会进入阻塞。
"""
import queue, time
from random import randint


class Production(threading.Thread):
    def run(self):
        while True:
            r = randint(0, 100)
            q.put(r)
            print('生产包子%s' % r)
            time.sleep(1)


class Proces(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print("吃掉包子%s" % re)


if __name__ == '__main__':
    q = queue.Queue()
    threads = [Production(), Production(),Production(),Proces()]
    for t in threads:
        t.start()
