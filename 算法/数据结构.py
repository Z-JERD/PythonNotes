"""
数据结构和算法的区别：
    算法是动态的,数据结构是静态的
列表、集合与字典等都是一种数据结构
程序=数据结构+算法
32位机器中1个整数占4个字节,64位占8个字节,1个字符占1个字节
其他语言的数组就是列表：
    申请的内存都是连续的,内存是按字节来划分的,比如100-119这一块内存,一共20个字节,能存放5个整数
    a[2] 其实列表名a存放的是起始地址100
    a[2]=100+2*4=108 即a[2]的值是内存108-112里面放的值
1.python中的列表：
    1.向列表中添加数据(append),内存不够,重新申请内存
        如果列表中的数据是同类型的,内存中的值就是真实的值,如果需要修改,就把此内存地址中的值抹掉重新赋值
    2.python中的列表可以添加不同的数据类型？
        如果列表中的数据是不同类型的,内存中的值存放真实值的地址,真实值存放在另外的内存种
        如果修改,会重新开辟内存来存放真实值,列表中真实值的地址也会发生变化
    3.列表中的元素是按照顺序来存储的
    4.列表按照下标读和写,时间复杂度是o(1)
        append 时间复杂度o(1)
        insert,delete 时间复杂度O(n)
2.栈(Stack)是一个数据集合,只能在一端进行插入或删除操作的列表。
    栈的特点：后进先出
    栈分为栈顶(表尾)和栈底(表头),在栈顶进行入栈(push)和出栈(pop)的操作
    在python中实现栈,使用列表结构即可
    进栈：append 出栈：pop 查看栈顶：li[-1]
3.队列(Queue):先进先出
    是一个数据集合,仅允许列表的一端进行插入,另一端进行删除 时间复杂度O(1)
    进行插入的一端称为队尾,删除的一端称为队头
    双向队列:队列的两端都允许进行进队和出队的操作
    使用列表完成队列：
        1.创建一个列表和两个变量，front变量指向队首，rear变量指向队尾。初始时，front和rear都为0。
        2.进队操作：元素写到li[rear]的位置，rear自增1。
        3.出队操作：返回li[front]的元素，front自减1。
    不足：删除后,数据前面会留下大量的空的内存
    解决方式：环形列表,将队首和队尾连接起来
        当队尾指针front == Maxsize + 1时,再前进一个位置就自动到0
        队满条件：(rear + 1) % MaxSize == front
    在python中实现,进队使用insert添加到索引为0的位置,出列使用pop







"""



"""
合并两个有序的数组,数组都是非递减的,合并后的数组依然有序

def merge(num1,m,num2,n):
    list=[]
    while m >0 and n >0:
        if num1[0] <= num2[0]:
            list.append(num1[0])
            num1.pop(0)
        else:
            list.append(num2[0])
            num2.pop(0)
    if m==0:
        list+=num2
    if n==0:
        list+=num1
    return list

反转数字：
def func(x):
    x=str(x)
    a=""
    if x.startswith("-"):
        a="-"
        x=x.strip("-")
    if x.endswith("0"):
        x=x.strip("0")

    for i in range(len(x)-1,-1,-1):
        a+=x[i]
    return int(a)
print(func(-123000))
一棵二叉树,逐层打印每一层节点

思路：1.为了打印当前节点的子节点,应该把子节点保存到容器中
     2.每一次打印一个节点时,如果该节点有子节点,就把子节点放到队列的末尾
     3.取出最先进入队列的节点
     
     def PrintForm(data)：
        if not data：
            return []
        result=[]
        tmp=[data]
        while len(data):
            cur=tmp.pop(0)
            result.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        return result

两个队列实现一个栈：
思路：
    进栈：1.队列中为空的添加数据
         2.如果都不为空,队列中值大于等于1的队列将数据删除,另一个队列添加删除的数据
    出栈：队列中存在着数据的删除
class Stack(object):
    
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,x):
        if len(self.stack1) == 0:
            self.stack1.append(x)
        elif len(self.stack2) == 0:
            self.stack2.append(x)
        if len(self.stack1)==1 and len(self.stack2) >=1:
            while self.stack2:
                self.stack1.append(self.stack2.pop(0))
        elif len(self.stack2)==1 and len(self.stack1) >1:
            while self.stack1:
                self.stack2.append(self.stack1.pop(0))
    def pop(self):
        if self.stack1:
            self.stack1.pop(0)
        elif self.stack2:
            self.stack2.pop(0)


"""

