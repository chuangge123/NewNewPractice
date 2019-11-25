# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/13
"""
  多行注释
"""
"""
编码与解码
    日本人把写好的代码转成unicode ————叫做编码encode
    中国人把这个转好的unicode 拿下来，想变成中文来观看，————叫解码 decode
    Unicode 需要先encode 成UTF-8  在dec
    Python3 开始默认编码为unicode
    s = "i am 哥斯拉"
    s1 = s.encode("gbk") encode 后面加的格式是你想转成码
    s2 = s1.decode('gbk') decode 后面加的是（当前是什么码）然后转成unicode
    print(s2)
    这里首先是，在python中程序编码默认就是unicode 
"""
"""
文件流
    f = open("文件名",'w',encoding = "utf-8") #这是写模式，读模式
    'r' read 模式 是文件已经存在，可以把文件内容 读取出来
    'w' write 模式 是文件已经存在，光标会从头开始进行写，如果文件不存在，就在默认目录下新建个文件，光标从头开始写
    'a' append 模式 是添加模式，是默认文件存在内容，光标出来默认在文件最后处开始。
    'r+' 读写模式。#写入的东西在所有内容最后的地方。
    'w+' 读写模式   # 写入东西，会把文件清空从新写。  
    f.close() #这是文件要关闭
二With 打开
    with open('文件名','w') as f:
        f.read()
        f.close()
    
相关操作
    f.read(5) 读取5个字符，光标停留在第六个字符。
    f.tell() 看光标在哪里， 一个中文站3个字符。
    f.seek(0) 调整光标的位置。 
    f.readline() 读取一行的内容
    f.readlines() 读取所有行，并存储到列表里。并且跑到了内存
    f.flush() 清空缓存
    f.truncate() 截断 （删除参数给的位置。）
    遍历时
    for i in f: 这是for内部将f对象做成了迭代器， 用一个取一个。
    
    str()可把任意数据类型转换为字符串，
    eval() 可把字符串引号去掉 转换回来。
    
"""

