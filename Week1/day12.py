# coding=utf-8
# __author:"NGLS Chuang"
# date: 2019/11/21
"""
正则
    re.findall('alex','dsafsdfsafalex') 按字符串匹配那么找 把所有的结果都返回到一个列表里
    re.search ("",'').group  只找到第一个符合条件的 就不继续往下找 返回一个对象，group 调用结果
    re.match()      只在字符串的开始匹配 返回一个对象也用group调用
    re.sub('a..x','s..b','hfjasalexdfhd')
    re.compile
    re.split('[j,s]','sdjksal')      通过字符j分割为两部分  j没了 早继续在子集用s分割
元字符**
    . 通配符    指代任意一个字符。
    ^ 尖角符    只在开始匹配
    $          只在结尾开始匹配
    *          重复匹配
    +          重复匹配 1到无穷个   b+ 对b 起作用
    ？         重复匹配 a?  [0-1]个a
    ()         重复陪陪 （1,3）  1-3个a   如果有四个a 则会匹配回3个 贪婪匹配。   （1，）  1到无穷。
    [] 字符集   1'[com,cn]' 匹配这两个，哪个都可以，是或的意思。2[a-z] 代表所有英文小写字符。
               3.取消元字符的特殊功能 (\ ^ -)'[w,*]'
               4.[^t] 除了t 都能匹配  [^4,5] 非4非5都行

    \          反斜杠后面跟元字符，去除特殊功能。 反斜杠跟部分普通字符实现特殊功能
    \d         匹配任何十进制数，相当于[0-9]
    \D         匹配任何非数字   [^0-9]
    \s         匹配任何白字符   [\t\n\r\f\v]
    \S         匹配任何非空白字符  [^\t\n\r\f\v]
    \w         匹配任何字母数字字符 [a-zA-Z0-9]
    \W         匹配任何非字母数字字符 [^a-zA-Z0-9]
    \b         匹配一个单词边界，也就是指单词和空格间的位置。 r'I\b' 匹配出这个单词，而有些单词里带I就不许匹配。
    把特殊意义的变为普通
    \. 就是匹配的是个.

    \\\\       表示一个\  或者 r'\\' 表示一个\

其他
    () 以括号来分组
    (as)+ 以as为一组进行匹配
    例子
    ret = re.search('(?P<id>\d(3))/(?P<name>\w(3))','weeew34ttt123/ooo')
"""
import re

#
# # ret = re.search('(?P<id>\d(3))/(?P<name>\w(3))', 'weeew34ttt123/ooo')
# # ret = re.search('(?P<id>\d+)/(?P<name>\w+)', 'weeew34ttt123/www')
# # print(ret.group())
# # print(ret.group('id'))
# # print(ret.group('name'))
# # # ?P<name> 这个是为后面内容进行分组 ，有点像字典。
# # print(1-2*((60-30)+(-40/5)*(9-2*5)))
#
# # 计算器小程序
# # 定义一个检测函数，检测里面有没有违法字符
# Flage1 = True
# while Flage1:
#     source = input('输入您需要计算的')
#
#
#     def check(s):
#         Flag = True
#         if re.findall('[a-zA-Z]', s):
#             print('请您输入数字')
#             Flag = False
#         return Flag
#
#
#     # 格式化空格等函数
#     def format(s):
#         s = s.replace(' ', '')
#         s = s.replace('++', '+')
#         s = s.replace('--', '-')
#         s = s.replace('**', '*')
#         return s
#
#
#     def cal_mul_div(s):
#         # 找到乘法或者除法的两个数的式子
#         ret = re.search('\d+\.?\d*\*\d+\.?\d*',s).group()
#         # 通过split 进行分割
#         x,y = re.split('\*',ret)
#         ret1 = float(x)*float(y)
#         str(ret1)
#         s.replace(ret,ret1)
#         return s
#
#
#     def cal_add_sub(s):
#
#         return s
#
#
#     def jisuan(str):
#         if check(source):
#             str = format(source)
#             # 遇到括号
#             while re.search('\(',str):
#                 # 查找最里层括号
#                 str = re.search('\([^()]\)', str).group()
#                 # 需要进行去括号，走函数
#                 str = re.sub('\(.+\)', '.+', str)
#                 str = cal_mul_div(str)
#                 str = cal_add_sub(str)
#             return str
#
#         else:
#             str = cal_mul_div(str)
#             str = cal_add_sub(str)
#             return str
# http://127.0.0.1:8000/Login
# ret = re.search('[a-zA-Z]+://[^\s]*[.com|.cn]','https://www.bai.com/shjdfhkjshdfdsauser=欢子').group()
# print(ret)
# '^(https?://\w+(?:\.[^\.]+)+(?:/.+)*/.+\.html\??(?:[^/]+=[^/]+)?(?:&[^/]+=[^/]+)*)?#?((?:/[^/]+)*)$'
# '^(https?://\w+)(?:\.[^\.]+)+(?:/.+)*/.+(\.html\?)?(?:[^/]+=[^/]+)?(?:&[^/]+=[^/]+)*?#?((?:/[^/,(\u4e00-\u9fa5)]+)*)$'
# ret = re.search('(https?://\w+)(?:\.[^\.]+)+(?:/.+)*/.+(\.html\?)?(?:[^/]+=[^/]+)?(?:&[^/]+=[^/]+)*?#?[^\u4e00-\u9fa5,/.]$','https://blog.csdn.net/wangchaoqi1985/article/details/82810471')
# print(ret.group())
# r'^(https?://\w+(?:\.[^\.]+)+(?:/.+)*/.+\.html)?#?((?:/[^/]+)*)$'
# ret = re.search(r'^(https?://\w+(?:\.[^\.]+)+(?:/.+)*/.+\.html)?#?((?:/[^/]+)*)','http://127.0.0.1:8000/Loginwangahuansjdfkjsdklhfklh旭辉哦').group()
# print(ret)
#
# string1 = 'http://127.0.0.1:8000/Loginwangahuansjdfkjsdklhfklhdsfsdhttps://blog.csdn.net/wangchaoqi1985/article/details/82810471'
# string2 = 'https://www.bai.com/shjdfhkjshdfdsauser=sddsfj'
# p = re.compile('^((https?://\w+)(?:\.[^/.]+)+(?:/.+)*/.+(\.html\?)?(?:[^/]+=[^/]+[^\u4e00-\u9fa5]+)?(?:&[^/]+=[^/]+[^\u4e00-\u9fa5]+)*?#?([^\u4e00-\u9fa5])$)')
# result1 = p.findall(string1)
# result2 = p.findall(string2)
# print(result1)
# print(result2)
# # ret= re.findall('alex', 'dsafsdfsafalex')
# print(ret)

# ret = re.findall('(^(https?://\w+)([^\.]+)+\.(?:[^\.]+)*.+(\.html\?)?(?:[^/]+=[^/]+)?(?:&[^/]+=[^/]+)*?#?[\u4e00-\u9fa5])','http://192.168.1.1')
# print(ret)
# ret = re.findall('(^(https?://)([^\.[\u4e00-\u9fa5]+)+\.(?:[^\.\u4e00-\u9fa5]+)+\.)','https://blog.csdn.net/wangchaoqi1985/article/details/82810471我曹乐https://blog.csdn.net/wangchaoqi1985/article/details/82810471')
# print(ret)
"""
ret = re.findall('[^\u4e00-\u9fa5]+', 'https://blog.csdn.net/wan温恩gchao我查看附件考虑i1985/article/deta我啊哈哦啊ils/82810471我曹乐')
print(ret)
str = ''
for i in ret:
    # print('%s %s'% (ret.index(i) + 1, i))
    str += i
print(str)
# print(''.join((a, b)))
"""
ret = re.findall('((https?://)([^\.[\u4e00-\u9fa5]+)+\.\w+\.\w+(\.)?\w+/)','https://blog.csdn.net/wangchaoqi1985/article/details/82810471我曹乐http://asdf.cggggghn.net/wangchaoqi1985/article/details/82810471http://192.168.1.1/winssf/fdsfdsf/dog.html')
print(ret)
# 2019.11.23
# 首先中文在正则中本来就是例外 \w 也会把中文获取到
# 在筛选url中，无法第一次用正则给筛除掉中文，
# 因为是按照头http头来进行筛选，是一条整体的字符。
# 只能在已经知道是url的条件下进行 筛除中文 ，并用for循环进行拼接