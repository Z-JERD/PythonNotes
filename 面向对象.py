#谈谈你对面向对象的理解？
'''
面向对象是一种编程思想,以类的眼光来看待事物的一种方式。一切皆对象,每个对象都有自己的属性,自己的行为。
在现实生活中的任何物体都可以归为一类事物,而每一个个体都是一类事物的实例
面向对象有三大特性:封装、继承和多态。
1.封装就是将方法和属性封装到类中,并对数据进行封装,使代码模块化,这样做使得代码的复用性更高。
2.继承则是进一步将一类事物共有的属性和行为抽象成一个父类，而每一个子类是一个特殊的父类--有父类的行为和属性,
也有自己特有的行为和属性。这样做扩展了已存在的代码块，进一步提高了代码的复用性。
3.多态则是为了实现接口重用。多态的一大作用就是为了解耦--为了解除i父子类继承的耦合度。
简单来说，多态就是允许父类引用子类对象。
'''
#类和对象的概念
'''
类：是对具有相同属性和相似行为的一类事物的抽象
属性：类 和 对象所拥有的的具体的"值"指标
对象：是一个具有具体属性值的类的实例化
'''
#什么是方法？类中可以定义哪几种方法？
'''
1.普通方法 2.属性方法 3.类方法 4.静态方法 5.私有方法 6.内置方法

'''
#什么是属性？类中可以定义哪几种属性？
'''
类和对象所拥有的具体的值
1.静态属性
2.动态属性                                                                                                                                                                                                                                                                                                                                                             
3.对象属性
4.私有属性
'''
#多态的概念：
'''
同一类事务有多种形态。多态的概念依赖于继承
新增类时,可以直接继承一个父类,对于父类中的方法,可以直接用也可以重写一个特有的
当子类和父类有相同的方法时，只会调用子类的。
'''
#python中的多态性
'''
不同对象接收同一条信息会产生不同的行为
多个不同的类具有共同的方法f，各个类调用方法f，返回值不同。
把方法f提取出来，封装为一个接口g。不同类的实例作为参数，传入接口g，得到不同返回值
class Dog(object):
    def talk(self):
        print('汪汪汪')
class Cat(object):
    def talk(self):
        print('喵喵喵')
def print_talk(obj):
    obj.talk()
d = Dog()
c = Cat()
print_talk(d)
print_talk(c)

python是自带多态的, 崇尚鸭子类型
    多个有相似特征的数据类型之间，不需要建立继承关系，而是通过约定俗成的方式来规范


'''
#Python面向对象中的继承有什么特点？
'''
1.python中的继承分为单继承和多继承
2.父类和子类拥有同名的方法时,子类的对象只会调用子类的
如果想要调用父类的方法,使用super
3.引用父类中的属性和方法时:
    1.使用单继承,会先从子类中寻找，子类中不存在，就去父类中找，直到最顶级的父类
    2.使用多继承会,先从子类中寻找,子类中不存在。会根据继承的顺序去查找
4.继承的作用:
    1.减少代码的重用
    2.提高代码可读性
    3.规范编程模式 
5.python3中的所有类都默认继承object

'''
#面向对象中super的作用？
'''
super在子类派生出新的方法,重用父类的功能
print(F.mro()) 查看继承顺序
1.在单继承中,super就是一直向上找父类
2.在多继承中,根据广度优先顺序找父类

'''
#什么是面向对象的mro
'''
方法解析顺序
对于支持继承的编程语言来说,其方法（属性）可能定义在当前类，也可能来自于基类，
当不知道继承顺序的情况下，可以使用这个来查找
'''
#如果查找一个对象的mro
'''
1先深度优先找到所有父类的继承树,再将其父类作为一个表
2取第一个表的头跟其他表的内容对比,如果没有重复的就取出来,并将这个类删除
如果有重复的就继续下一个表的表头与其它表的内容对比
3.如果不能比较就会报错(循环继承)

'''
#面向对象深度优先和广度优先是什么？
'''
1.深度优先 广度优先 都是一种遍历算法,把所有的项都走一遍,且不会重复
深度优先,先沿一条线走,当前线走完之后,再走其他的线。主要体现在经典类在多继承的情况下查找属性的方式
广度优先,顺着一条线查,还有别的路能走到目标处，就终止这条路,换一条线查。主要体现在新式类在多继承的情况下查找属性的方式
B和C继承A，D继承B，E继承C，F继承D，E
广度优先的顺序：1.F 2.D 3.B 4.E 5.C 6.A
深度优先的顺序：1.F 2.D 3B. 4.A 5.E 6.C 
2.在经典类和新式类的应用:
    经典类和新式类的区别：
      经典类  遵循 深度优先算法 且没有mro方法  python2
      新式类  继承object 遵循 广度优先算法 有mro方法   python3
      在python中如果把经典类变成新式类，在最顶级父类类名加上(obj)
'''
#静态方法和类方法区别？
'''
1.装饰器不同,类方法@classmethod,静态方法@staticmethod
2.类方法中有一个默认的参数cls,而静态方法没有
3.调用的时候都不需要实例化
3.静态方法 : 相当于在类作用域下的普通函数,不进行与类或实例相关的操作
  类方法 : 由类调用,进行与类有关的操作
'''
#什么是反射？以及应用场景？
'''
通过字符串来获取对象的属性或方法甚至获取类
如：rest framework里面的CBV,根据用户请求方式的不同,通过反射调用对应的函数,实现不同的操作
'''
#metaclass作用？以及应用场景？
'''
metaclass是生产类的类,通过它来控制类的产生同时建类时能够自动地改变类
场景：
1.在模块里将所有的类的属性都设置成大写形式。有好几种方法可以办到，
但其中一种就是通过在模块级别设定__metaclass__。采用这种方法，这个模块中的所有类都会通过这个元类来创建，
我们只需要告诉元类把所有的属性都改成大写形式
例：
    def upper_attr(name,parent,attr):
        attrs=dict((name.upper(),value) for name,value in attr.item 
        return type(name,parent,attrs)
    __metaclass__ = upper_attr
    class Foo(object):
        也可以只在这里定义__metaclass__，这样就只会作用于这个类中
        bar = 'bip'
print hasattr(Foo, 'bar')  False
print hasattr(Foo, 'BAR') True
2.元类的主要用途是创建API,比如Django ORM
models.Model定义了__metaclass__
允许像这样定义：
    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()
3.创建单例模式
4.使用抽象类时
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):   Payment就成了接口类
    @abstractmethod
'''
#用尽量多的方法实现单例模式
'''
1.使用__new__
import threading
class Singleton(object):
    _instance_lock=threading.Lock()
    _instance=None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super(Singleton,cls).__new__(cls,*args, **kwargs)
        return cls._instance
2.使用元类
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
Python2
class MyClass(object):
    __metaclass__ = Singleton
Python3
class MyClass(metaclass=Singleton):
   pass
3.使用装饰器
from functools import wraps
def outer(cls):
    instances={}
    @wraps(cls)
    def inner(*args,**kwargs):
       if cls not in instances:
           instances[cls]=cls(*args,**kwargs)
       return instances[cls]
    return inner
@outer
class Singleton():
    pass
4.模块的导入
模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件,直接取上次执行后的结果
5.使用类：
import threading
class Singleton(object):
    _instance_lock=threading.Lock() #解决多线程问题
    def __init__(self):
        pass
    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            Singleton._instance=Singleton(*args,**kwargs)
        return Singleton._instance
  
'''
#列举面向对象中带双下划线的特殊方法
'''
1.__init__  初始化方法 给已经创建出来的对象添加属性初始化方法
2.__new__   构造方法  创造一个对象
3.__del__   析构方法: 对象的被删除之前调用的方法
4._call__   对象后面+()直接调用call方法，此方法python独有
            类后面加()调用执行init方法，对象后面()直接调用call方法
5.__str__   如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值
6.__repr__  如果一个类中定义了__repr__方法，那么在打印对象时，默认输出该方法的返回值
            __str__是面向用户的，而__repr__面向程序员
7.__item__系列 操作a['name']这种形式
8.__attr__系列 操作a.name 这种形式
'''
#如何判断是函数还是方法？
'''
看是如何调用的
1.函数是封装了一些独立的功能,可以直接调用,可以传参,可以有返回值,也可以没返回值
2.方法和函数类似，同样封装了独立的功能,但是方法是需要通过对象来调用的
    1.方法中的数据是隐式传递的；
    2.方法可以操作类内部的数据
3.判断类型,如果时function就是函数 method就是方法

'''
#异常处理写法以及如何主动抛出异常
'''
1.为什么要进行异常处理:
    程序中的异常会导致程序不再继续运行了
2.写法：
    try:执行语句
    except 异常类型:触发异常后执行的语句
    else：没有触发异常执行的语句
    findlly:有没有异常都执行的语句
万能异常:Exception,当finally遇到return的时候 finally仍然执行
3.主动抛异常(可自定义异常类型)
    raise 异常类实例   
'''
#什么是断言？应用场景？
'''
Python的assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假,则会抛出AssertError并且包含错误信息
这个异常通常不会去捕获它.我们设置一个断言目的就是要求必须实现某个条件

应用场景：
    1.断言是常用于开发阶段的工具，用来测试代码,是一种很方便的单元测试方法
    2.使用断言的方式是检查程序的不变量.
        如果你的函数希望在它开始时有数据库的连接，并且承诺在它返回的时候仍然保持连接，这就是函数的不变量
    3.按约定进行设计。函数与调用者之间有个约定
        如果传的非空字符串，保证将字符串的第一个字母大写并返回
'''
#isinstance作用以及应用场景？
'''
判断一个对象是不是某个类的实例
isinstance(obj,cls)判断obj是否是类cls 的对象
'''
#有用过with statement吗？它的好处是什么？( python中的with语句的作用？)
'''
在文件操作的时候用过,with语句的作用是通过某种方式简化异常处理
好处：
1.with语句在嵌套的代码执行之后,会自动关闭文件
2.无论嵌套的代码以何种方式结束,它都会关闭文件。
  如果嵌套的代码发生异常，with会在外部捕获这个异常之前关闭文件
3.如果嵌套的代码中有continue/return/break语句,它同样能够关闭文件

上下文管理器即需要实现两个方法：_enter_()和_exit_(); 
_enter_():负责进入代码块的准备工作，进入前被调用； 
_exit_()：负责离开代码块的善后工作，离开后被调用；
class Context(object):
		def __enter__(self):
			print("do something before")
			return self
		def __exit__(self,exc_type,exc_val,exc_tb):
			return print("do something after")
		def do_something(self):
			return print("do something")
	with Context() as ctx:
		ctx.do_something()
	python执行with-as 的时候 会调用__enter__方法，然后该函数的返回值传给as后指定的变量，
	之后会执行with-as 下面的代码块，无论该代码块中出现了什么异常，都会在离开时候执行__exit__
	__exit__也可以做一些异常的监控和捕获。

'''










