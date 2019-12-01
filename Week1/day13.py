# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/25
"""
if __name__ = __main__ 函数的作用
    该函数的作用是在功能函数中测试执行。
    如果调用该功能函数的模块时，是不会执行调用的模块。
"""
"""
json 模块。
    就两个方法
    一个是json.dumps() 加载过去
    另一个json.loads() 加载回来
    举例代码
    存
    dic = {'name':'sunchuang','age':'18'}
    f = open('json_text',w)
    data = json.dumps(dic)
    f.write(data)                  18.19行可替换为 json.dump(dic,f)
    f.close()
    取
    dic = {'name':'sunchuang','age':'18'}
    f = open('json_text',r)
    data1 = f.read()
    data = json.loads(data1)       24.25行可替换为 data = json.load(f)
    print(data['name'])
pickle 模块
    pickle 也是 dumps和loads 但是存储的函数。
    注意，可以序列化函数。 loads 时必须本模块必须也有函数才能序列化出来用。
shelve 模块。 
    shelve 主要是方便存储后进行修改
    存
    f = shelve.open('Shelve_text')
    f['info'] = {'name':'sunchuang','age':'18'}
    取
    f = shelve.open('Shelve_text')
    data = f.get('info')
    print(data)
XML 模块
    import xml.etree.ElementTree as ET
    tree = ET.parse('xml_test')    解析xml
    root = tree.getroot() 获取到根标签对象
    print(root.tag) 再获取根标签属性
    # root.tag 为标签名。root.attrib 为标签的属性
    遍历xml文档(查询)
    for child in root:
        print(child.tag,child.attrib)
        for i in child:
            print(i.tag,i.text)
    修改直接改 或者网上查，xml不常用
    删除
    root.remove(名称)
"""
"""
面向对象
    class Bar:
        def foo(self,arg):        self 也就是 obj
            print(self,self.name,arg ) 输出：  obj的地址 ， obj的name也就是'SunChuang'， 传入的参数666
    
    obj = Bar()   此时foo 中的self就是 obj
    obj.name = 'SunChuang'  这里吧name变量封存到对象之中 即为封装（。。。python的封装是真的lllllow）
    obj.foo(666)
self
    self 中 是谁调用该函数，self就是谁（对象）
构造方法
    class Bar:
        def __init__(self,name,age): 添加构造方法时, 再调用这个类时，需要把参数传递给构造函数
            self.n =name   接收 self  (lizi1)传的参数，赋值给 lizi1的n 变量 把变量还是储存到中间人（对象）的内存里 
            self.a = age
        def show(self):
            print('%s-%s' %(self.n,self.s))
    lizi1 = Bar('李欢',18)

继承
    class Father:
        def basketball(self):
            pass
    class Son(Father)
        def baojian(self):
            pass
    
    重写：即不会执行父类的方法，执行自己的。
    Super 代指父亲的类。
        super(当前类的类名，self).父类的方法
        父类名.父类的方法（self） 这个self需要自己添加下，系统不会自己创建。
    **python 可以 多继承
    如下
    Class Son(Father1,Father2):  在子类查找父类方法的时候，会从左到又查找。（2）如果出现查找的父类上还有父类会按当前分值继续查找。
        pass                  （3）:如果是有共同的跟父类  会先查每条分支的底层，最后查找公共的根。   
    obj = Son()
    obj.方法
    
多态
    Python 里 多态可以忽略。因为傻瓜语言嘛
    
"""

# 练习主要练习self.属性 过多不练。
# import time
#
#
# class Person:
#     def __init__(self, n, a, g, f):
#         self.name = n
#         self.age = a
#         self.xueliang = g
#         self.fight = f
#
#     def fighthim(self):
#         print('即将战斗')
#         time.sleep(3)
#         self.xueliang = self.xueliang - 20
#         self.fight = self.fight + 30
#         print('战斗结束血量下降20，当前血量剩余%d' % self.xueliang)
#         print('战斗力增长30，当前战斗力为%d' % self.fight)
#
#
# rol_list = []
# y_n = input('是否创建角色')
# if y_n == 'y':
#     name = input('请输入名字')
#     age = input('请输入年龄')
#     xueliang = int(input('输入血量'))
#     fight = int(input('战斗力多少'))
#     member = Person(name, age, xueliang, fight)
#     rol_list.append(member)
#     for i in rol_list:
#         print(i.name)
#     flag = True
#     while flag:
#         y_f = input('是否战斗')
#         if y_f == 'y':
#             member.fighthim()
#         else:
#             flag = False
"""
在 init 方法里 创建的 字段（self.name）属于普通字段，是属于对象的，只能通过对象访问
在类里直接定义的字段 属于 静态字段。 对象，类都可以访问 

静态方法
    class Foo:
        @staticmethod  就是加个装饰器   
        def bar(): 静态方法可以没有self
            print('我是静态方法')

类方法
    class Foo:
        @classmethod
        def classmethod(cls): cls 是class的缩写。 也就是类名，可以直接通过类来执行。
            print('我是类方法')

@property
属性方法
    
    调用的时候 只需要 obj.方法名字     不用加括号
@属性方法名.setter         是为 属性方法赋值。
    方法名也要与属性方法名相同 
    obj.perr =123  即可设置    
    
"""
