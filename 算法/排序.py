#时间复杂度和空间复杂度
'''
1.时间复杂度
    用来估计算法运行时间的一个式子
    一般来说,时间复杂度高的算法比复杂度低的算法慢
    复杂度效率排序：
    O(1)<O(logn)<O(n)<O(nlogn)<O(n2)<O(n2logn)<O(n3)
    一般的时间复杂度：
        1.循环减半的过程：O(logn)
        2.几次循环就是n的几次复杂度
2.空间复杂度：
用来评估算法占用内存的大小
'''
#递归和二分查找
'''
递归的两个特点：
    1.调用自身
    2.结束条件
例1：执行下面的代码,输出结果：
def func(x):
    if x>0:
        print(66)
        func(x-1)
        print(x)
func(3)  #66 66 66 1 2 3
例2：用递归打印出：抱着抱着抱着我的小鲤鱼我的我的我的
def func(x):
    if x>0:
        print("抱着",end="")
        func(x-1)
        print("我的",end="")
    else:print("我的小鲤鱼",end="")
func(3)
3.汉诺塔移动:
h(n)=2h(n-1)+1
count=0
def func(x,a,b,c):
    if x>0:
       global count
       count+=1
       func(x-1,a,c,b)
       #查看移动的顺序
       print("%s-->%s"%(a,c))
       func(x-1,b,a,c)
    return count
print(func(4,'a','b','c'))
4.一段有n个台阶组成的楼梯，小明从楼梯的最底层向最高处前进，它可以选择一次迈一级台阶或者一次迈两级台阶。
问：他有多少种不同的走法？
取决于最后一步是跨一个台阶还是另个台阶
f(n-1)+f(n-2)
def func(n):
     if n <= 2:
        return n
    else: return func(n-1)+func(n-2)
print(func(5))

'''
#二分查找
'''
1.列表查找：从列表中查找指定元素
    元素下标
2.顺序查找
    从列表第一个元素开始，顺序进行搜索，直到找到为止。
3.二分查找
列表必须是有序的
通过对待查找的值与候选区中间值的比较可以使候选区减少一半。
def func(li,var):
    low=0
    high=len(li)-1
    while low<=high:
        mid=(low+high)//2
        if li[mid]==var:
            return mid
        elif li[mid]>var:
            high=mid-1
        else:
            low=mid+1
    return None
li=list(range(0,100,3))
print(func(li,6))
使用二分查找的时间复杂度：O(logn)
使用递归：时间复杂度是O(n)
    def find(l,aim,start=0,end=None):
        if end == None:end = len(l)-1
        if start <= end:
            mid = (end - start) // 2  + start
            if l[mid] > aim:
                return find(l,aim,start=start,end=mid-1)
            elif l[mid] < aim:
                return find(l,aim,start=mid+1,end=end)
            elif l[mid] == aim:
                return mid  #返回给了上一级
        else:
            return None

'''
#列表的排序：将无序列表变为有序列表
#排序low B三人组
'''
时间复杂度:O(n2)  空间复杂度：O(1)
冒泡排序
选择排序
插入排序
    冒泡排序：时间复杂度：O(n2) 最好情况 o(n)
        对列表每相邻的两个数比较,如果前边的比后面的大就交换两个数,比较到最后一个数后，
        再回来重新比较
        代码关键点：
            趟：每遍历一趟,有序区多一个数,无序区少个数
            无序区
            import time
            def cal_time(func):
                def wrapper(*args,**kwargs):
                    t1=time.time()
                    result=func(*args,**kwargs)
                    t2=time.time()
                    print("%s running time: %s sexs."%(func.__name__,t2-t1))
                    return result
                return wrapper
            @cal_time
            def func(li):
                for i in range(len(li)-1):
                    #第i趟
                    for j in range(len(li)-1-i):
                        #j 箭头位置
                        if li[j] > li[j+1]:
                            li[j+1],li[j] =li[j],li[j+1]
            import random
            li=list(range(100))
            random.shuffle(li)
            func(li)
            
            冒泡排序-优化
            如果冒泡排序中执行一趟而没有交换，则列表已经是有序状态，可以直接结束算法。
            @cal_time
            def func(li):
                for i in range(len(li)-1):
                    exchange=False
                    for j in range(len(li)-1-i):
                        #j 箭头位置
                        if li[j] > li[j+1]:
                            li[j+1],li[j] =li[j],li[j+1]
                            exchange = True
                    if not exchange:
                        return
    选择排序：时间复杂度：O(n2)
        1.一趟遍历记录最小的数,放到第一个位置
        2.再一趟遍历记录剩余列表中最小的数,继续放置
        代码关键点：
            1.无序区
            2.最小数的位置
        def func(li):
            for i in range(len(li)-1):
                min_loc=i
                for j in range(i+1,len(li)):
                    if li[j] < li[min_loc]:
                        min_loc=j
                if min_loc !=i:
                    li[i],li[min_loc]=li[min_loc],li[i]
    插入排序:最好情况O(n)在左手上的牌总是排序好的   最坏情况O(n2)
        1.列表被分为有序区和无序区两部分,最初有序区只有一个元素
        2.每次从无序区选择一个元素,插入到有序区的位置,直到无序区变空
        关键点：
        [5,7,4,3,6,1,2,9,8]
        def insert_sort(li):
            for i in range(1,len(li):
                tmp=li[i]  #摸到的牌
                j=i-1  #手里牌的个数
                while j>=0 and tmp <li[j]:
                    li[j+1] =li[j]
                    j=j-1
                li[j+1]=tmp        
'''
#排序NB三人组：
'''  
时间复杂度 o(nlogn)
快速排序
堆排序
归并排序
    快排:最好情况o(nlogn) 最坏情况 O(n2)
    总共要排logn趟 每趟的时间复杂度都是n
    最坏：要排n趟，没趟的时间复杂度都是n
    最好情况O(n*logn)——Partition函数每次恰好能均分序列
    最坏情况O（n^2）,每次划分只能将序列分为一个元素与其他元素两部分:
    输入的元素已经排序或逆向排序
    排序从小到大的时候  100 99 98 97 ... 5 4 3 2 1这样的就是最坏的了
    即选的基数要么是最大的要么是最小的
        1.取一个元素p(第一个元素),进行整理
          整理后的列表被p分为两部分,左边的都比p小,右边的都比p大
        2.使用递归完成排序
        快排的最坏情况:在python中使用递归时有最大深度限制
        修改 sys.setrecursionlimit(20000)
        def partition(data, left, right):
            tmp = data[left]
            while left < right:
                while left < right and data[right] >= tmp:
                    right -= 1
                data[left] = data[right]
                while left < right and data[left] <= tmp:
                    left += 1
                data[right] = data[left]
            data[left]=tmp
            return left
        def quick_sort(data,left,right):
            if left < right:
                mid =partition(data,left,right)
                quick_sort(data,left,mid-1)
                quick_sort(data,mid+1,right)
        import random
        li=list(range(1000))
        random.shuffle(li)
        quick_sort(li,0,len(li)-1)
        print(li)
    堆排序：
        1.建立堆
        2.得到堆顶元素，为最大元素
        3.去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
        4.堆顶元素为第二大元素。
        5.重复步骤3，直到堆变空。
    归并排序：
        一个列表分两段有序,将其变为有序的操作成为归并操作
        如：[2,5,7,8,9,1,3,4,6] 9之前的一段有序，9之后的一段有序
        def merge(li,low,mid,high):
            i=low
            j=mid+1
            ltmp=[]
            while i <=mid and j <= high:
                if li[i]<=li[j]:
                    ltemp.append(li[i])
                    i+=1
                else:
                    ltmp.append(li[j])
                    j+=1
            while i <=mid:
                ltmp.append(li[i])
                i+=1
            while j<=high:
                ltmp.append(li[j]) 
                j+=1
            li[low:high+1] = ltmp
        li=[2,5,7,8,9,1,3,4,6]
        merge(li,0,4,len(li)-1)
        print(li)
一般情况下,运行时间:
快速排序---归并排序---堆排序
三种算法的缺点:
快排：极端情况下排序效率低
归并排序：需要额外的内存开销
堆排序：在快的排序算法中相对较慢

'''
#其它排序
'''
希尔排序
计数排序
桶排序
基数排序
    希尔排序:分组插入排序算法  最好的情况o(n1.3) 最坏的o(n2)
        1.首先取一个整数d1=n/2,将元素分为d个组,每组相邻元素的下标之间的距离为d,在各族内进行插入排序
        2.取第二个整数d2=d1/2,重复上述分组排序过程，直到di=1
        希尔排序每趟不使某些元素有序,而是使整体数据越来越接近有序,最后一趟排序使所有数据有序
    计数排序：时间复杂度O(n)
        建个空列表存放每个元素出现的次数。将原列表中的值作为新列表中的索引
        这样就数据就有序了
        def count_sort(li, max_num):   
            count = [0 for i in range(max_num + 1)]
            for num in li:
                count[num] += 1
                i = 0
                for num,m in enumerate(count):
                    for j in range(m):
                        li[i] = num
                        i += 1
    桶排序：
        在计数排序中，如果元素的范围比较大(比如在1到1亿之间)就要用到桶排序
        首先将元素分在不同的桶中,在对每个桶中的元素排序。
        平均情况时间复杂度：O(n+k)
        最坏情况时间复杂度：O(n2k)
    基数排序:多关键字排序：
        有一个员工表，要求按照薪资排序，薪资相同的员工按照年龄排序
        先按照年龄进行排序，再按照薪资进行稳定的排序。
        时间复杂度：O(kn)
        空间复杂度：O(k+n)
        (k表示数字位数)
'''


