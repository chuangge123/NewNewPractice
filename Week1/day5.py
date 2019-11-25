# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/11
"""
  多行注释
"""
"""
  修改字体大小，背景颜色在 settings—— Editor—— Font
  修改创建py文件时，自动生成日期在  Editor——File and Code——Python Script 
  
"""
# 小程序
# name = input("Name:")
# age = input("Age:")
# salary = input("Salary")
# # 判断一下是否是数字类型的字符串
# if salary.isdigit():
#     # 把自己转成数字
#     salary = int(salary)
# else:
#     print("必须是数字才行")
# print(name, age, salary)
"""
  占位符 %s s=string
        %d d=digit
        %f f=float
"""
"""
  for 循环详解
  range(3)——为0,1,2
  range(1,3)—— 为1,2
  range(1,101,2)步长为2，结果都是奇数
  for i in range(3):每次把i自动进行+1   ！！！ range(1,10) 则 取不到10. 1到9 正常 range(10) 是0——9
  for i in 内容（可迭代对象，序列）          可迭代的对象，都有__iter__()方法。
"""
"""
  元组
  1.如果创建单个元素的元组，则必须在后面加，例如a=(23,)
  2.元组的查询 也可以用切片print(a[1:2])
  3.元组 不能修改 直接赋值， 例如 a[1]=5 则会报错

"""
"""
集合
    s = set('Sun Chuang')    输出{'n', 'c', 'g', 'u', ' ', 'h', 's', 'a'}
    因此 集合最重要的是去重
    set（里面必须是可以哈希的）
    通过In 去判断元素是否在里
    print(u in s)则为true
    添加元素 用的方法为add() s.add()
    s.update（‘spt’） 会把每个字母变为元素在后面添加上。
    s.remove('n') 删除元素
    s.pop()  随机的删除
    s.clear() 清空
    相关操作
    print(set('alex')==set('alexexex'))   True
    set('alex')<set('alexwwww')  True
    a|b                a&b                                               a-b
    and 联合(并集)    or （交集）
    union()=同上       intersection =or    a.intersection(b)    a.difference(b) 指a里面有的b里面没有
    父集(a.issuperset(b))        子集a.issubset(b)      
"""
"""
   列表的增删改查
   列表创建方式，
   1.a=[1,2,3]
   2.a=list((1,2,3))
   第一个括号为方法带的。
   
   a=['wuchao','xiaohai','guli','shanben','lilei']
   想要找出索引
   a[3]———— 对应的是shanben
   1.切片取范围值（查）
   a[1:3]   ————切片顾头不顾尾 取出的值为 xiaohai , guli     3则不取。
   a[1:]  ————1到最后的元素  
   a[1:-1] ————1到倒数第二个值
   a[1::2]  a[1:-1:2]  ————1到最后一个值，1到倒数第二个值 隔一个值一取（步长为2）
   a[3::-1]   ————代表从第三个开始倒着取
   
   2.append insert (增)
   a.append('xuepeng')———— 会在列表的最后添加这么一个人 （默认最后）
   a.insert(1,'xuepeng')————  指定位置添加
   
   3.改
   a[1] = 'haidilao'——————重新赋值即可。
   a[1:3] =['a','b'] ———— 多个修改
   
   4.删除
   del a[0] 直接删除
   a.remove('xiaohai')————删除固定的值
   a.pop(1)———— 删除索引的值,并返回给你。举例如下。
   b=a.pop(1) ———— 此时b 的值就是'xiaohai' 
   
   5.其他操作
   5.1. count 操作 
       例 a.count('to') 计算一个列表中count 出现几次
   5.2. extend 
       将数组进行相加
       例 a = [1,2,3] b = [4,5,6]  a.extend(b)
          print(a)  输出 a为[1,2,3,4,5,6]
   5.3. index 
        可以通过内容找到索引号
        例：print(a.index('xiaohai'))  打印为1
   5.4. reverse
        sort
        从大到小 ，与从小到大的排序。
    5.5深度拷贝
       s=[1,'ads','advin']
       s2=s.copy()
    

6.作业—— 购物车小程序
  先让用户输入工资
  打印个购物菜单
  循环买东西
  salary = 5000
  1. iphone11 5800
  2. mac book 9000
  3. coffee   32
  4. watch    1500
"""
# 程序代码如下
# print('您输入的余额')
# yue = int(input())
# print('欢迎来到11会场，以下您可购买的商品')
# shangpin = ['1.iphone11  $5800/n', '2.mac book  $9000/n', '3.coffee   $32/n', '4.watch    $1500/n']
# print(shangpin)
# print('请输入数字进行购买')
# flag = True
# while flag:
#     print('请输入数字进行购买')
#     one = int(input())
#     if one == 1:
#         if yue - 5800 < 0:
#             print("余额不足,可输入其他数字购买其他的")
#
#         else:
#             print('已经加入购物车，余额为：')
#             yue = yue - 5800
#             print(yue)
#     elif one == 2:
#         if yue - 9000 < 0:
#             print("余额不足")
#         else:
#             print('已经加入购物车，余额为：')
#             yue = yue - 9000
#             print(yue)
#
#     else:
#         flag = False
#         print('已经退出')
"""
  上面自己写的，下面是答案的代码（利用了嵌套）***补for循环
"""
product_list = [
    ('Mac', 9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 105),
    ('bike', 2000),
]
saving = input('please 输入你的余额')
if saving.isdigit():
    saving = int(saving)
    # for i in product_list:
    #     print(product_list.index(i), i)
    # ！ 这里使用了enumerate——枚举（列表，从1开始）
    # for i in enumerate(product_list,1):
    #     print(i)
    # 通过两个变量 跑 这个product_list i对应编号 v对应product_list 里的属性
    """
      科普一下
      如果两个变量接收一个列表 那么这里的元素分别付给两个值,例子如下：
      a,b=[2,3]  那么a=2：b=3
    """
    flag = True
    while flag:
        for i, v in enumerate(product_list, 1):
            print(i, '>>>>', v)
        choice = input('选择购买商品编号[退出:q]:')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice < len(product_list):
                p_item = product_list[choice - 1]
                # 去取一个a元组，a列表的值只需要 a[i]就能取到了
                price = p_item[1]
                price = int(price)
                if saving - price < 0:
                    print('余额不足请充值')
                else:
                    saving = saving - price
                    mingcheng = p_item[0]
                    print('您购买的商品', mingcheng, '成功')
                    print('您的余额为', saving)

            else:
                print('请您输入正确商品编号')

        elif choice == 'q':
            flag = False
            print('退出')
        else:
            print('请输入正确的数')
else:
    print('请您输入正确的数')
