#什么是正则的贪婪匹配？
'''
贪婪匹配:总是尝试匹配尽可能多的字符,*,+,?等都是贪婪匹配
后面加?号使其变成惰性匹配
b = re.findall('xx.*xx',secret_code)   # 贪婪匹配
非贪婪匹配,尽可能少的匹配
c = re.findall('xx.*?xx',secret_code)  # 非贪婪匹配
'''
#re中match以及search有什么区别
'''
相同点：1.都接收两个参数，第一个参数为正则表达式，第二个参数为待匹配的字符串
       2.只匹配一个符合条件的项
不同点：search根据所写的正则表达式匹配出第一个满足条件的项
       match  根据所写的正则表达式从头开始匹配，相当于在正则表达式开始的位置加一个^
'''
#如何生成一个随机数
'''
使用random 模块
1.随机小数
    1.random.random()  在0<=n<1之间生成一个随机浮点数
    2.random.uniform(n,m) 在指定范围生成一个随机浮点数
2.随机整数
    1.random.randint(n,m) 在指定范围生成一个随机整数
    2.random.randrange(n,m,x) 按指定基数递增的集合中获取一个随机数
3.从序列中获取一个元素
    random.choice(m) m为str/list/tuple
4.从序列中获取多个元素
    random.sample(m,x) m为str/list/tuple x为str
5.将一个列表中的元素打乱
random.shuffle(list)
'''
#os和sys模块的作用？
'''
os模块:
    负责程序与操作系统的交互,提供了访问操作系统底层的接口
    常用方法:
        1.os.getcwd() 获取当前工作目录
        2.os.listdir("dirname") 列出自定目录下的所有文件和子目录
        3.os.mkdir("dirname") 生成目录
        4.os.remove(path) 删除一个文件
        5.os.path.split(path)  将path分成目录和文件名的元祖
            os.path.split("/zhao/python/11.txt")   #('/zhao/python', '11.txt')
        6.os.path.join(name1,name2) 将多个路径组合后返回
sys模块:
    负责程序与python解释器的交互，提供了一系列的函数和变量,
    用于操控python运行时的环境
    常用方法:
        sys.argv           命令行参数List，第一个元素是程序本身路径
        sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
        sys.version        获取Python解释程序的版本信息
        sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
        sys.platform       返回操作系统平台名称
'''
#time模块
'''
1.时间有三种表示方式:
    1.1时间戳(给计算机看的）           
    1.2格式化的字符串(人能够看懂的时间)    
    1.3结构化时间(操作时间的)  
时间戳-->结构化时间
time.gmtime(时间戳)    #UTC时间，与英国伦敦当地时间一致
time.localtime(时间戳) #当地时间
time.localtime(1500000000) 不写参数默认当前时间的时间戳
结构化时间-->时间戳　
time.mktime(结构化时间)
time_tuple = time.localtime(1500000000)
time.mktime(time_tuple)

结构化时间-->字符串时间
time.strftime("格式定义","结构化时间")  结构化时间参数若不传，则默认当前时间
time.strftime("%Y-%m-%d %X")
time.strftime("%Y-%m-%d",time.localtime(1500000000))
字符串时间-->结构化时间
time.strptime(时间字符串,字符串对应格式)
time.strptime("2017-03-16","%Y-%m-%d")
time.strptime("07/24/2017","%m/%d/%Y")
'''
#如何使用python删除一个文件？
#json的作用
'''
1.网络传输：能在网络上传输的只能是bytes和字符串
    dumps和loads 进行网络传输
2.数据持久化
    dump load用在文件操作数据类型的序列化与反序列化上

'''
# json序列化时，可以处理理的数据类型有哪些？如何定制支持datetime类型？
'''
1.数字
2.字符串
3.列表
4.集合
5.布尔值(True-->true False---->false)
6.None(None-->null)

自定义时间序列化转换器
import json
from json import JSONEncoder
from datetime import datetime
class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(‘%Y-%m-%d %H:%M:%S‘)
        else:
            return super(ComplexEncoder,self).default(obj)
d = { ‘name‘:‘alex‘,‘data‘:datetime.now()}
print(json.dumps(d,cls=ComplexEncoder))
# {"name": "alex", "data": "2018-05-18 19:52:05"}

'''
#json序列化时,默认遇到中文会转换成unicode,如果想要保留留中文怎么办？
'''
dumps时指定ensure_ascii=False
例:
dic={"name":"python开发"}
print(json.dumps(dic))   {"name": "python\u5f00\u53d1"}
print(json.dumps(dic,ensure_ascii=False))  {"name": "python开发"}
'''
#logging模块的作用？以及应用场景？

