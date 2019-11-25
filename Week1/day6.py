# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/12
"""
  多行注释
"""
"""
 字典
  a=10
  b=a
  b=15
  这里需要讲一个点，a=10,a=5 是在内存空间内创建一个a=10的空间而a的指针指向10 ，后又创建一个a=5的空间，这时a的指针又指向5.而那个10的空间还是存在的
  
  不可变类型：整形，字符串，元组
  可变类型：列表，字典
  总结：就是看开辟的内存是否可被修改。
  字典定义
  dic={''}
  dic2=dict((()))
  dic6=dict.fromkeys(['host1',host2,'host3'],'test') 这个创建字典时会把列表中每一个作为一个key ,而所有都是一个value
  字典存储的键值对是无序的，
  在取值时，通过dic['key'] 则可对应这个的值
  字典两大特点：无序，键唯一
  
  
   
    字典的相关操作方法
    1.增加
    dic1={'name':'alex'}
    dic1{'age'}=18       则会吧这个键值对进行了添加。
    setdefault 
    dic1.setdefault{'age',34}
    该方法是 对dic1中的键值对进行检查，如果有age这个键，那么就不做任何变动，如果没有则会添加一个这样的键值对。
    如果用一个值去接收它，那么就会接收到原来age的
    2.查的话 基本都是通过key 查找对应的value
    查找对应的key 可以通过 dic1.keys()  如果想用的话可以通过 list(dic1.keys())编程列表进行操作
    同理查找所有的value list(dic1.values()),会打印所有的值。
    3.改
    dic1{'age'}=26...
    dic1.update(dic4) 该方法是把dic4字典的键值对加入，如果有重复则会覆盖。
    4.删除
    del dic1{'name'} 删除该索引下的键值对
    dic1.clear() 对字典进项清空。
    dic1.pop('age')  删除索引对应的值，并把值返回 
    5.嵌套字典的操作
      修改 dic1[key1][key2][1]='要改的内容'
    6.字典的排序
      sorted(dic1)  根据键的数字由小到大的排序，字符串英文也是 dic1.value()  可以根据值来排序
    7.字典的遍历
      for i in dic1
        print(i,dic1[i])
      for i in dic1.items():
        print(i)
"""
"""
字符串
    1.字符串可以用切片输出
    比如：print('helloworld'[2:])
    2.关键字 in 可以判断字符串是否存在某个字符串， 存在True 反之
    3.字符串格式化，print('%s is a good'%'alasl')
    4.字符串的正确拼接 c=''.join([a,b])
字符串的常用内置方法
    1.st='hello world'
    print(st.count('l'))查看个数
    2.print(st.capitalize())将字符串首字母大写
    3.print(st.center(50,'-'))一共打印50个- 把字符串放中间
    4.print（st.encode()）
    5.print(st.endswith('y'))是否是以这个字符串结尾
    6.print(st.startswith('y'))是否是以这个字符串开头
    7.print(st.find('o'))查找某一个字符的位置并且返还给我们
    8.print(st.index('w')) 返回值6
    7.print('sad'.isalnum())查看是否是字母
    8.print()
"""

menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                'CCTV': {},
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {},
            },
            '三里屯': {
                '优衣库': {},
                '苹果': {},
                '艾比': {},
            },
        },
        '昌平': {
            '沙河': {
                '沙河居委会': {},
                'oldboy': {},
                '阿泰包子': {},
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
                '社区': {},
            },
            '回笼馆': {
                '优衣库': {},
                '苹果': {},
                '艾比': {},
            },
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                '快手': {},
            },
            '中观村': {
                '优酷': {},
                '爱奇艺': {},
                '腾讯': {},
            },
            '五棵松': {
                '华西': {},
                '二院': {},
                '医院': {},
            },
        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CCIC': {},
                '高盛': {},
                '摩根': {},
            },
            '外滩': {},
            '郊区': {},
        },
        '文行': {
        },
        '静安': {
        },
    },
    '山东': {
        '济南': {},
        '德州': {
            '乐陵': {
                '定乌镇': {},
                '城区': {},
                '艾比下乡': {},
            },
            '平原': {},
            '庞德': {},
        },
        '青岛': {},
    }
}
"""
  要求可以 一层一层进入到所有层
  可以在每层返回到上一层
  可以在任一层推出
"""
# flag = True
# while flag:
#     print('选择那您的省份/或直辖市')
#     # 第一层循环出北京等市单位
#     for city in menu:
#         print(city)
#     choice = input('>>:').strip()
#     if choice in menu:
#         while True:
#             # 循环出区和市的单位
#             for city2 in menu[choice]:
#                 print(city2)
#             choice2 = input("输入市,返回上一层请输入exit>>:").strip()
#             if choice2 in menu[choice]:
#                 while True:
#                     # 循环出三里屯
#                     for city3 in menu[choice][choice2]:
#                         print(city3)
#                     choice3 = input("输入乡及场所,返回上一层请输入exit:").strip()
#                     if choice3 in menu[choice][choice2]:
#                         while True:
#                             for city4 in menu[choice][choice2][choice3]:
#                                 print(city4)
#                             choice4 = input('返回上一层请输入exit')
#                             if choice4 == 'exit':
#                                 break
#                     elif choice3 == 'exit':
#                         break
#             elif choice2 == 'exit':
#                 break
#             else:
#                 print('输入正确省份')
#
#     else:
#         print('请输入正确省份')
"""
下面是简化版的代码。
"""
# 定义一个当前层 ,思路是 每次循环的小字典 都赋值给这个current_layer
current_layer = menu
parent_layer = []
# 回退思路 就是把没进入一层的父层添加到列表里，这样我们只需要，在回退时把这个值pop并删掉取出来进行操作即可
while True:
    for city in current_layer:
        print(city)
    choice = input('>>>:').strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice =="exit":
        # 这句话就代表 parent_layer不为空就是true 反之
        if parent_layer:
            current_layer = parent_layer.pop()
        else:
            print('到头了，别按了')

    else:
        print("无此项")
