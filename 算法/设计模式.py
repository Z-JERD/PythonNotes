设计模式的六大原则
""""
1.开闭原则：扩展是可以的,对修改关闭,修改是不允许的
2.接口隔离原则：使用多个专门的接口,不使用单一的总接口
3.单一职责原则:简单来说一个类只负责一项职责
4.里氏替换原则：引用基类(父类)的地方必须透明的使用子类的对象
5.依赖倒置原则：高层模块不应该依赖低层模块,要针对接口编程，而不是针对实现编程
6.迪米特法则:：一个软件实体应当尽可能少地与其他实体发生相互作用
"""

设计模式
"""
简单工厂模式
工厂方法模式
创建者模式
单例模式


1.简单工厂模式：通过一个工厂类来负责创建产品类的实例
优点：隐藏了对象创建的实现细节,客户端不需要修改代码
缺点:1.将多个创建逻辑放到了一个工厂类里,违反了单一职责原则
     2.添加新产品是时,需要修改工厂类的代码,违反了开闭原则
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元" % money)


class PaymentFactory:
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "applepay":
            return ApplePay()
        else:
            raise NameError(method)
2.工厂方法模式：每个具体产品对应一个具体的工厂
适用场景：1.需要生产多种、大量复杂对象的时候
         2.需要降低耦合度的时候
缺点：每增加一个具体产品类，就必须增加一个相应的具体工厂类

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)


class PaymentFactory:
    def create_payment(self):
        raise NotImplementedError


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()


af = AlipayFactory()
ali = af.create_payment()
ali.pay(120)


3.抽象工厂模式:每个具体工厂都生产一套产品。
例：生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。
    对每个具体工厂,分别生产一部手机所需要的三个对象。
适用场景：提供一个产品类库，想隐藏产品的具体实现时
优点：1.将客户端与类的具体实现相分离
      2.每个工厂创建了一个完整的产品系列，使得易于交换产品系列

缺点：难以支持新种类的（抽象）产品
------抽象产品------

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ------抽象工厂------

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ------具体产品------


class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("iOS系统")


# ------具体工厂------


class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# ------客户端------


class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()



def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)


p1 = make_phone(MiFactory())
p1.show_info()
4.建造者模式：将一个复杂对象的构建与它的表示分离
主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。
------产品------

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.arm, self.body, self.leg)


#------建造者------


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def get_player(self):
        pass


class BeautifulWomanBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = "漂亮脸蛋"
    def build_arm(self):
        self.player.arm="细胳膊"
    def build_body(self):
        self.player.body="细腰"
    def build_leg(self):
        self.player.leg="长腿"
    def get_player(self):
        return self.player


class PlayerDirector:
    def build_player(self, builder):
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        builder.build_body()
        return builder.get_player()


pd = PlayerDirector()
pb = BeautifulWomanBuilder()
p = pd.build_player(pb)
print(p)
5.单例模式：
保证一个类只有一个实例

依赖于继承的创建型模式：工厂方法模式
依赖于组合的创建性模式：抽象工厂模式、创建者模式

"""


