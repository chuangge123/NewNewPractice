# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/19
"""
  多行注释
"""
import os

"""
time模块
    import time
    print(time.time())#1574153907.1359737 时间戳
    time.sleep() 休息
    time.clock() 计算CPU执行的时间。
    time.localtime 本地时间         print（help(time.strftime)）可以显示方法的函数
    struct_time = time.localtime()
    print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))
     按这种格式显示日期。
    print(datetime.datetime.now())
"""
"""
random 模块
    import random
    print(random.randint(1,8)) 随机生成1-8的数
    random.choice('helwoj') 随机使用一个字母
    random.randrange(1,8)

"""
"""
os 模块 *******
    os.getcwd()获取当前工作目录
    os.chdir() 改变当前的工作目录 需要+r 路径
    os.curdir  返回当前目录（.）
    os.pardir  获取当前目录的父目录字符串名('..')
    os.makedirs ('abc\\alex')  创建多层的文件夹（递归生成）
    os.removedirs('dirname')  只能删除空的文件夹
    os.mkdir('文件夹名')  在当前目录下创建一个文件夹  '\\表示什么目录下 在创建一个文件夹'
    os.rmdir('')  删除当前这个文件夹。
    os.listdir(r'')  把文件and文件夹都存入到一个列表里。r就是源生字符串，防止路径下有\n等特殊含义的字符起作用。
    os.remover()删除一个文件
    os.rename("oldname","newname")重命名文件/目录
    os.stat('path/filename') 获取文件信息 其中主要 st_size文件大小
    os.sep  查看在当前系统表示目录层级用什么（Window用 \）
    os.linesep 获取行终止符 Win \t \n 
    os.pathsep  获取路径分隔符，Win 下为：
    os.system("") 执行shell 命令
    os.environ   获取环境变量
    os.path.abspath('./abc')  把相对路径转为绝对路径。
    os.path.dirname(path)  把当前编译的文件上一级文件夹的路径获取到 **
    os.path.join ([a,b]) 进行路径拼接。
    
"""
"""
sys 模块
    该模块是跟python解释器进行交互
    sys.argv 在程序执行时可以传入一个列表[文件名 参数1 参数2]
    sys.path.append() 加入路径，我们自己添加模块的
    sys.path 返回模块的搜索路径，
"""
"""
hashlib 模块
    m=hashlib.md5()
    m.update('hello world'.encode('utf-8')) python3中默认都是unicode 类型，这里需要byte 类型所以给转为utf8
    print(m.hexdigest())
    以上代码进行字符串加密。
    
    sha256() 也是同样加密调用。  无法转回去。
"""
"""
logging 模块
    import logging
    logger = logging.getLogger()
    #创建一个handle,用于写入日志文件。
    fh = logging.FileHandler('test.log')
    #创建一个handle,用于输出到控制台。
    ch =logging.StreamHandler()
    logging.basicConfig(level = logging.INFO  (这里可以是DEBUG，主要是设置级别的),
    format = '%(asctime)s - %(filename)s[line:%(lineno)d]  %(levelname)s - %(message)s',
    datefmt = '%a,%d %b %Y %H:%M:%S',   设置时间格式
    filename = 'test.log',
    )
    logger = logging.getLogger(__name__)
    
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
    
    2.将日志输出到文件里
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
    
    3.参数
    %(levelno)s：打印日志级别的数值
    %(levelname)s：打印日志级别的名称
    %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s：打印当前执行程序名
    %(funcName)s：打印日志的当前函数
    %(lineno)d：打印日志的当前行号
    %(asctime)s：打印日志的时间
    %(thread)d：打印线程ID
    %(threadName)s：打印线程名称
    %(process)d：打印进程ID
    %(message)s：打印日志信息
"""
"""
configparser 模块
    
    read(filename) #读取配置文件，直接读取ini文件内容
     
    sections() #获取ini文件内所有的section，以列表形式返回['logging', 'mysql']
     
    options(sections) #获取指定sections下所有options ，以列表形式返回['host', 'port', 'user', 'password']
     
    items(sections) #获取指定section下所有的键值对，[('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('password', '123456')]
     
     get(section, option) #获取section中option的值，返回为string类型
     >>>>>获取指定的section下的option <class 'str'> 127.0.0.1
     
    getint(section,option) 返回int类型
    getfloat(section, option)  返回float类型
    getboolean(section,option) 返回boolen类型
"""