# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/18
"""
  多行注释
"""
"""
装饰器
    为你之前的函数添加新的功能
    @ show_time  #foo = show_time(foo)
    def foo():
        print('foo')
        time.sleep(2)
        
    def show_time(f):
        def inner():
            start = time.time
            f()
            end = time.time
            print("spend %s"%(end - start))
        return inner   #这里 把inner的内存地址给返回出来  inner是一个变量，不加()不会执行
    foo = show_time(foo)
    不用装饰器  则 foo()调用即可， 这样也就实现了同名调用，但是该函数功能增加了。
    实际上就是执行inner 函数了 ，inner 函数里面已经执行了foo()
装饰器参数
    def logger(flag):
        def show_time(f):
            def inner():
                start = time.time
                f()
                end = time.time
                print("spend %s"%(end - start))
            return inner   #这里 把inner的内存地址给返回出来  inner是一个变量，不加()不会执行
        return show_time
    
    这样写由于闭包的作用 show_time 可以使用到flag
    这样写也就是相当于加了一个变量
    @logger("true")
"""


# 装饰器编写登录


def logintest(flag):
    def login(fun):
        def inner(*args, **kwargs):
            if flag == "false":
                print("您需要登录")
                username = input("username:")
                password = input("password:")
                if username == "sunchuang" and password == "sunge123":
                    flag == "true"
                    print("welcome dear sunchuang")
                    ret = fun(*args, **kwargs)
                    return ret
                else:
                    print("账号密码不正确")
            else:
                print("您还没有登录")

        return inner

    return login


def home():
    print("欢迎来到京东超市")
    print('选择您的商品去提交')


@logintest("false")
def 添加购物车():
    print('购物车已经成功添加')


@logintest("false")
def jiesuan():
    print('结算成功')

home()
添加购物车()
jiesuan()