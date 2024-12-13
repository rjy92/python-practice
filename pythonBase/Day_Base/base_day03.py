#循环中断 break  本次循环中断 continue 开始下次循环
str1="abc123" #打印1前边的内容 不可用find
for i in str1:
    if i == "1":
        break #退出循环
    else:
        print(i)
else:
    print("完成了") #break 中断的循环此句不会被执行

#不知道循环次数时 死循环+break
#请任意多个值,直到输入 0时停止
while True : #不做控制直接写死循环(循环条件永远满足)
    s=input("请任意值,输入 0则停止")
    if s=="0":
        break #当输入的值为0时 ,中断

str1 = "abc123" #打印str1的字符除1外(1不打印)
for i in str1:
    if i!="1":
        print(i)
for i in str1:
    if i=="1":
        continue #不用管我,打印下一吧 ,结束本次循环开始下一次循环
    print(i)

假设一个用户信息如下:
   用户名是:root
   密码是: 123456
写一个身份验证的程序myprog4.py，让用户输入用户名和密码登录,
用户名和密码全部匹配，提示登录成功。
否则继续，最多尝试3次。3次不匹配以后提示登录失败.

循环3次,密码正确可中断
05 回来

cishu = 3
while cishu>0:
    user_name=input("请输入用户名")
    user_password=input("请输入密码")
    cishu=cishu-1 #当输入完用户密码就表示已经用完一次机会
    if user_name=="root" and user_password=='123456':
        print("登录成功")
        break #登录成功中断循环(不需要其它机会了)
    else:
        if cishu != 0:
            print("输入错误,还有{}次机会".format(cishu))
        else:
            print("机会用完,可操作忘记密码")

容器类型: 列表list  集合set  元组 tuple 字典 dict
python 中一个变量只能绑定一个数据对象，
当有大量的数据需要存储时，可以使用python给我们提供的容器类型的数据，
容器内部可以存储大量的数据，并可以实现相应的运算。

列表 list 类型符号[]
特点:
1.存储任意多个任意元素
2.元素存储有顺序(通过索引(位置)访问)
3.可变容器(可修改_加元素,减元素,改元素值)
定义:
1.直接给值
l1 = [1,1.1,"abc",True] #可存任意多个任意元素
l2 = [] #创建一个空列表
l3 =[1,"abc",l1,l2]
print(l1)
print(l3)
2.类型转换:通过关键字list 实现
str1 = "abc123"
range1=range(5)
print(list(str1)) #把字符串的每个字符转化为list的元素
print(list(range1)) #把range的范围值做为元素
l1= list() #创建一个空列表


访问: 索引左侧从0开始,右侧从-1开始 格式:变量名[索引|切片]
1.索引直接访问
l1 = [1,1.1,"abc",True]
print(l1[1],l1[-1]) #访问列表中的第二个和最后一个
2.切片:获取多个数据元素
[开始索引:结束索引:步长]
开始索引可省默认为0,结束索引可省默认到最后,步长可省默认为1
开始索引:结束索引 之间是 左闭右开(包含开始位置的值,不包含结束位置的值)
步长为正数时从左向右获取数据, 步长为负数时从右向左获取数据

打印l1从第二个开始的所有元素
l1 = [1,1.1,"abc",True]
print(l1[1:])

打印l1除了第一个,最后一个所有元素
l1 = [1,1.1,"abc",True]
print(l1[1:-1])

修改:可变容器(可修改_加元素,减元素,改元素值)
改元素值:在访问的基础上直接赋值
l1 = [1,1.1,"abc",True]
l1[1] = 1.2 #单个元素修改
print(l1)
l1[1:-1] = [3,"ab","cc","dd"] #多个元素修改(可能出现删除或增加元素)
print(l1)
加元素
1.最后加单个元素:  list变量名.append(元素)
l1 = [1,1.1,"abc",True]
l1.append("de")
l1.append(["abc",1.5])
print(l1)
2.在指定位置插入单个元素: list变量名.insert(位置,元素)
l1 = [1,1.1,"abc",True]
l1.insert(1,3.1415)
l1.insert(2,[10,100])
print(l1)
3.在最后加多个元素:list变量名.extend(可迭代对象)
把可迭代对象展开,各元素放入list中
l1 = [1,1.1,"abc",True]
l1.extend(["abc",1.5])
l1.extend("abc")
l1.extend(range(5))
print(l1)
删除
清空:list变量名.clear()
l1 = [1,1.1,"abc",True]
l1.clear()
print(l1)
根据元素值删除:list变量名.remove(元素值) 删除找到的第一个元素值
l1 =[5,"bac",5,3.1415]
l1.remove(5)
print(l1)
根据位置删除: del list变量名[索引],
list变量名.pop([索引]) 给索引就删除指定索引位置的值,没给索引则删除列表的最后一个元素
pop删除指定位置的元素并返回删除的元素内容
del l1[-1]
print(l1)

l1 =[5,"bac",5,3.1415]
pop1=l1.pop() #删最后一个
pop2=l1.pop(1) #删除第二个元素(索引为1)
print(l1,pop1,pop2)

查找
1. 查找某元素的位置
list变量名.index(元素值,[start[,end]]),第一个相同元素出现的位置,找不到则报错
l1 =[5,"bac",5,3.1415]
print(l1.index(5))
print(l1.index(5,1))
print(l1.index(5,1,2)) #从索引1向后找到索引2且不包含索引2
2. 查找容器中是否包含某个元素
元素值 in list变量名    包含为True,不包含为False
元素值 not in list变量名   不包含为True 包含为False
l1 =[5,"abc",5,3.1415]
print("abc" in l1)
print( 5 not in l1)
3. 查找某元素值在容器中出现的次数 list变量名.count(元素值)
l1 =[5,"abc",5,3.1415]
print(l1.count(5))

练习
1. 定义一个列表元素有a-g ,0-9 名为l1
l1 = list("abcdefg" )
l1.extend(range(10))
print(l1)
#2. l1中移出元素0 remove
l1.remove(0)
print(l1)
#3. l1中移出第3个元素  pop del
l1.pop(2) # del l1[2]
print(l1)
#4. 从l1中提取出奇数索引的元素值并保存到l2中 (切片 步长)
l2 = l1[1::2]
print(l2)
#5. 向l2的最后添加元素值2
l2.append(2)
print(l2)
#6. 向l2的最后追加此列表中的值[5,7,2]
l2.extend([5,7,2])
print(l2)
#7. 修改l2中第一个b元素值为2  找到b的位置index, 访问基础上直接赋值
b_index=l2.index("b")
l2[b_index] = 2
print(l2)
#8. 删除l2中所有值为2的元素 remove  count
i=1
c=l2.count(2)
while i<=c:
    l2.remove(2)
    i=i+1
print(l2)  #15 回来

其它:
运算: 连接(+),重复 *
l1=[1,2,3]
l2=["a","b","c"]
print(l1+l2, l1*3)
补充常用函数：
列表元素逆序: 切片或reverse;
l1=[1,2,3]
print(l1[::-1])
l1.reverse()
print(l1)
列表元素排序: 列表变量名.sort(reverse=False)
#reverse=False 表升序，True 表倒序
l1=[1,5,3,9,7]
l1.sort(reverse=True) #reverse默认为False(列表元素为升序)
print(l1)
复制列表内容: 列表变量名.copy()
l1=[1,5,3,9,7]
l2=l1.copy()
l1[1]= 10
print(l1,l2,id(l1),id(l2))
#id(变量名）查看变量在内存中的地址

元组 关键字tuple 符号()
特点：
1.任意多个任意元素
2.元素顺序存储(可以通过索引访问)
3.容器不可变(不能修改_改变元素值，添加元素，删除元素)
定义：
直接给值
t1=(1,1.5,True,"abc",[1,2,"a"])
print(t1)
类型转换
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple(range(5)))
访问:
直接访问：索引左侧从0开始，右侧从-1开始
t1=(1,1.5,True,"abc",[1,2,"a"])
print(t1[2])
print(t1[-1])
切片访问： [开始索引:结束索引:步长]
开始索引可省默认为0，结束索引可省默认到最后， 步长可省默认为1
步长为正是向右获取，步长为负是向左获取
开始索引:结束索引  是左闭右开(包含开始，不包含结束)
#1.t1中偶数索引的元素
t1=(1,1.5,True,"abc",[1,2,"a"])
print(t1[::2])
#2.t1中前3个元素
print(t1[:3])

查找：
1.某个元素所在的位置
元组变量名.index(元素值[,开始位置[,结束位置]]) 第一个元素所在的位置
找不到会报错
t1=(1,1.5,True,"abc",[1,2,"a"],1.5)
print(t1.index(1.5))
print(t1.index(1.5,2))
2.某元素值在tuple中出现的次数 元组变量名.count(元素值)
t1=(1,1.5,True,"abc",[1,2,"a"],1.5)
print(t1.count(1.5))
3.判断元素是否在元组中
t1=(1,1.5,True,"abc",[1,2,"a"],1.5)
print(1 in t1)
print(2 not in t1)

运算：连接(+) ,重复(*)
t1=(1,1.5,True,"abc",[1,2,"a"],1.5)
t2 =(1,2,3)
print(t1+t2, t2*2)

#1.定义一个list元素a~f， 定义一个tuple元素是 0-8
l1=list("abcdef")
t1=tuple(range(9))
print(l1,t1)
#2.把tuple中的后3个元素放入到list中
l1.extend(t1[-3:])
print(l1)
#3.tuple中的元素，有几个在list中出现过
shu=0
for i in t1:
    if i in l1:
        shu=shu+1
print(shu)


练习
1. 定义一个list ，求list元素的众数(频数最多的那个元素)
l1 =[1,2,1,3,4,3,1,3,3]
mode=-10  #记录最多的元素值
shu=0 #记录出现最多的元素个数
for i in l1:
    if l1.count(i)>shu: #比以前元素出现个数多了，保存出现的次数及元素值
        shu=l1.count(i)
        mode=i
print(mode,shu)
#2.对list 去重 （空list, l1 通过not in 判断后放到空list中）
l2=[]
for i in l1: #遍历L1
    if i not in l2: #此元素不在l2中，则加到l2中
        l2.append(i)
print(l2)
#3.l1中元素的平均值 (元素总和/元素个数)
l1 =[1,2,1,3,4,3,1,3,3]
print(sum(l1)/len(l1))

复习
1. 循环相关指令
    break ：中断循环
    continue:停止本次循环，开始下次循环
2. 容器类型：可以存放多个元素
    list 列表：
    特点：1.可存放任意多个任意类型元素
         2.元素按顺序存储
         3.容器可变
         4.关键字 list,符号 []
    定义(存储数据):
         1.直接赋值 变量名=[元素1,元素2,..]
         2.类型转换 list(可迭代对象)
         3.空list : [] 或 list()
    访问(获取数据):
         1.直接访问： 变量名[索引]
         2.切片器： 变量名[开始索引:结束索引:步长]
    修改:
         1. 修改指定位置的元素值：
            在访问的基础上直接赋值
         2. 添加元素
            结尾追加单个元素  变量名.append(元素)
            指定位置插入单个元素 变量名.insert(元素)
            结尾处追加多个元素 变量名.extend(可迭代对象)
         3. 删除元素
            根据元素值删除 变量名.remove(元素值)
            根据索引删除 变量名.pop([索引])  del 变量名[索引]
            清空容器 变量名.clear()
    查找:
         1. 查找指定元素值的位置 变量名.index(元素值,[开始位置[,结束位置]])
         2. 查找指定元素值是否在list中   元素值 [not] in 变量名
         3. 查找指定元素值在list中个数  变量名.count(元素值,[开始位置[,结束位置]])
    运算: 拼接(+) 重复(*)
    其它常用函数:
        1. 逆序 变量名.reverse()
        2. 排序 变量名.sort([reverse=True|Fasle])
        3. 复制 变量名.copy()

序列容器常用函数
    元素个数: len(变量名)
    元素求和: sum(变量名)
    元素求最大: max(变量名)
    元素求最小: min(变量名)


    tuple 元组
    特点:
        1.可存放任意多个任意类型元素
        2.元素存储有顺序
        3.容器不可变
        4.关键字 tuple  符号()
    定义(存数据)
        1. 直接赋值:  变量名=(元素1,元素2,..)
        2. 类型转换:  变量名=tuple(可迭代对象)
    访问(获取数据)
    、  1. 直接访问： 变量名[索引]
        2. 切片器： 变量名[开始索引:结束索引:步长]
    查找
        1. 查找指定元素值的位置 变量名.index(元素值,[开始位置[,结束位置]])
        2. 查找指定元素值是否在tuple  元素值 [not] in  tuple
        3. 查找指定元素值在tuple中个数 变量名.count(元素值,[开始位置[,结束位置]])
    运算: 拼接(+) 重复(*)



