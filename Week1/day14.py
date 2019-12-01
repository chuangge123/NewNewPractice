# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/28
"""
成员修饰符
    self.__age = age 此处__后面加上变量名 该变量为 ‘私有’ 也就是只能在类的内部看到
    可以是建立一个方法，给return 出来，但是执行这个方法可以设置验证。
    和java一样 私有的 是继承不了的。
"""
"""
特殊成员 
    例如: __init__ 构造方法
    
    2.def __call__(self,*args,**kwargs) 这个是当调用对象的时候,会自动执行该方法。
    obj = Foo()   
    obj()        也可以是Foo()() 也是等于前面的两步。
    
    3.def __str__
    例子
    class Foo:
        def __init__(self,s,a):
            self.name = s
            self.age = a
        def __str__(self):
            return '%s-%s' %(self.name,self.age)
    obj = Foo('alex',18)
    print(obj)   print——> str(obj) ——>__str__ 并获取其返回值。
    结果 alex-18
    
    4. __int__       int(对象)
    
    5. __add__   两个对象相加时，自动执行第一个对象的__add__方法，并且将第二个对象当做参数，传递进入
    
    6. __del__   析构方法 ，就是对象在被销毁时 ，会自动调用这个方法。
    
    7. __dict__  将对对象中封装的所有东西，通过字典的方式进行返回
    例子：
        class Foo:
            def __init__(self,name,age):
                self.name=name
                self.age =age
                self.sex ='男'
        obj = Foo('alex',18)
        d = obj.__dict__    把对象里的所有成员‘注释也算’ 给封装到字典
        f = Foo.__dict__    把类的对象的所有成员 给封装到字典。
        print(d)
    
    8.__getitem__(self,item):
        return item+10       把对象变成列表索引那样处理
    例子:
        class Foo:
            def __init__(self,name,age):
                self.name = name
                self.age = age
            def__getitem__(self,item): #获取值方法
                return item+10
            def__setitem__(self,key,value):
                print(key,value)       #赋值
            def__delitem__(self,key):
                print(key)
        li = Foo('sunchuang',18)
        r = li(8)            对象（给一个参数） 会自动执行这个__getitem__ 函数
        print(r)    18
        li[100] = 'asdf'    100 asdf
        del li(999)
        
    9.__iter__   把对象变为可迭代的
    例子
    class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __iter__(self):
        return iter([11,12,13])

    li = Foo('sunchuang','18')
    for i in li:
        print(i)
        
    
"""
'''
异常处理
    try:
        pass              （raise Exception ） 主动触发异常。
    except Exception as e:  错误信息封装作为e 
        出错后逻辑。
    
    可以自定义  让一个类继承这个 Exception 
    
'''
'''
反射
    python 的反射效率高，而且很方便
    
    hasattr(obj,'name')       检测一下obj中有没有name成员
    getattr(obj,'name')       获取到 obj中 name 对应的值。
    setattr(obj,'key','value')  设置对象新的成员。
    delattr(obj,'name')       删除
'''


# 模拟 url 进行访问。
# class Foo:
#     def __init__(self):
#         self.name = 123
#
#     def f1(self):
#         return '首页'
#
#     def f2(self):
#         return '新闻'
#
#     def f3(self):
#         return '个人页'
# s2 = Foo()
# inp = input('输入url')
# func = getattr(s2,inp)
# resulf =func()
# print(resulf)
"""
单利模式
    对象只创建一份，省内存。
    数据库链接池
"""