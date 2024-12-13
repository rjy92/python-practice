容器类型；字典 dict
    特点:
         1.可变的容器
         2.元素存放无序(以键(key)-值(value)对存放,key value的分隔符:,key唯一)
         3.关键字 dict 符号 {}
定义：
    1.直接赋值：
dict1={"name":"gu","age":18,"sex":"女"}
dict2={"name":"gu","score":[50,60,70]}
dict3={"name":"gu","score":{"数学":50,"英语":60,"语文":70}}
dict4=dict(name="gu",age=18,sex="女")
print(dict1,dict2)
print(dict3,dict4)
    2.类型转换（dict每个元素有两部分组成 key，value)
l1=[["name","gu"],["age",18],["sex","女"]]
print(dict(l1))
t1=((1,"一"),(2,"二"),(3,"三"))
print(dict(t1))

访问:
1. 访问单个元素：通过key访问
dict3={"name":"gu","score":{"数学":50,"英语":60,"语文":70}}
t1=((1,"一"),(2,"二"),(3,"三"))
d1 = dict(t1)
print(dict3["score"],d1[3],dict3["score"]["英语"])
#print(d1[4]) #key 不存在是报错
字典变量名.get(key,"key不存在时的提示信息")
print(d1.get(3,"没有key=4的元素"))
2. 访问所有key 或 所有 value
dict3={"name":"gu","score":{"数学":50,"英语":60,"语文":70}}
print(dict3.keys(),dict3.values())

修改(添加，删除，修改元素值)
修改元素值：在访问的基础上直接赋值
dict1={"name":"gu","age":18,"sex":"女"}
dict1["age"] = 28
print(dict1)
添加元素:
     1.添加单个元素 变量名[新key]
dict1={"name":"gu","age":18,"sex":"女"}
dict1["city"] = "北京"
print(dict1)
     2.添加多个元素 变量名.update({元素1,元素2,...}) 参数里的字段有则更新，无则添加
dict1={"name":"gu","age":18,"sex":"女"}
dict1.update({"数学":70,"age":80})
print(dict1)
     3.删除元素
清空
dict1={"name":"gu","age":18,"sex":"女"}
dict1.clear()
print(dict1)
del :访问前直接加del
dict1={"name":"gu","age":18,"sex":"女"}
del dict1["sex"]
print(dict1)
pop: 通过key 删除: 删除指定元素的同时返回value
dict1={"name":"gu","age":18,"sex":"女"}
print(dict1.pop("age"))
print(dict1)
查找：
    判断元素值是否在容器里： 元素值 [not] in 字典

遍历：看看每个元素 可迭代
方法一：
dict1={"name":"gu","age":18,"sex":"女"}
for i in dict1: #i是每个元素的key
    print(i,dict1[i])
方法二:
dict1={"name":"gu","age":18,"sex":"女"}
for k,v in dict1.items(): #item 是没个元素 k,v是此元素key和value
    print(k,v)
方法三:
dict1={"name":"gu","age":18,"sex":"女"}
for i in dict1.keys(): #遍历字典的Key
    print(i,dict1[i])



set集合:1.去重存储 2.集合运算(交集，并集，差集)
    特点:
    1.可变的容器但集合内元素不可变的(只能做增减，元素值不能变)
    2.相当于只有键没有值的字典(每个元素只有一部分组成,元素唯一)
    3.元素无序的存储结构(无需访问)
    4.关键字 set  符号{}
定义:
1.直接给值：
    s1 = {"a","b","c"}
    print(s1)
2.类型转换:
    l1=[1,2,1,3]
    t1=(1,2,4,2)
    print(set(l1),set(t1),set("abccd"))
3.空set
    s1 = set()
    print(s1)

集合运算:交集，并集，差集
s1={1,2,3}
s2={1,2,4}
print(s1 & s2) #& 交集
print(s1 | s2) #| 并集
print(s1-s2,s2-s1) #- 差集
print(s1^s2) #^对称差

修改：只能做元素的增(变量名.add(元素) 减(clear,remove,pop)
s1={1,2,3,"aa","cc",-10}
s1.add(4)
print(s1)
s1.remove(1) #删除指定的元素
print(s1)
print(s1.pop()) #随机删除
print(s1)
s1.clear()
print(s1)

查找：
    判断元素值是否在容器里： 元素值 [not] in 集合

输入字符串，输出字符串中出现次数最多的字母及其出现次数。
如果有多个字母出现次数一样，
则按字符从小到大顺序输出字母及其出现次数。
str1="deacfacb"
#1. str1去重  === deacfb
set1 = set(str1)
print(set1)
#2. 遍历去重结果  每个字符出现的次数放入字典中
dict1={}
for i in set1:
    dict1[i]=str1.count(i)
print(dict1)
#3. 字典中所有值的最大值  2 len,max,min,sum
count_max = max(dict1.values())
print(count_max)
#4. 对所有的key 排序 abcdef
list1=list(dict1.keys())
list1.sort()
print(list1)
#5. 以abcdef顺序，找值为 2的元素
for i in list1:
    if dict1[i] == count_max:
        print(i,count_max)


自定义函数：封装代码,提高代码的重用行
定义：
def 函数名([形参名1,形参名2,..]): #函数名命名遵守变量名命名规则
    函数体
    [return 返回值]

两个数值相加 add_test
def add_test(shu1,shu2):
    he = shu1+shu2
    return he
#调用:
print(add_test(10.5,11.8))

两个数的最大值
def max_test(shu1,shu2):
    max_shu = -100 #只是为了生名一个变量
    if shu1>shu2:
        max_shu=shu1
    else:
        max_shu=shu2
    print(max_shu)

print(max_test(100,500))

#自定义函数 is_zhishu 实现判断一个数是否为质数(只能被自己和1整除的数)
#返回值 是True，否False
def is_zhishu(shu):
    for i in range(2,shu): #2~shu-1之间
        if shu % i == 0:  #有被整除的
            return False  #不是质数
    return True #以上循环中没有return走，证明shu 为质数
print(is_zhishu(7),is_zhishu(4))
#调用函数实现打印出50-150之间的质数
for i in range(50,151):
    if is_zhishu(i):
        print(i)
自定义函数返回两个容器的交集(容器可是list,tuple,set  或字符串)
def get_jiaoji(rongqi1,rongqi2):
    rq1 = set(rongqi1)
    rq2 = set(rongqi2)
    return rq1 & rq2
print(get_jiaoji([1,2,3],[1,2,4]))
print(get_jiaoji((1,3,5),(2,3,5)))
print(get_jiaoji("abch","bcdef"))
print(get_jiaoji({"a":1,"b":2,"c":3},{"a":5,"d":1}))

a=set(str1)                              #set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
count={}
#遍历集合a
for i in a:
    count[i]=str1.count(i)       #count()函数统计字符串str中的各个字符出现的次数。
#统计字典中最大的values
max1 = max(count.values())
# items()函数以列表返回可遍历的(键, 值)元组数组
data = list(count.items())
# 将元组以字母顺序对列表进行排序：
data.sort()
# 判断元组values是否等于最大值，满足则输出对应字母字符及出现次数
for i in data:
    if i[1] == max1:
        print(i[0], i[1])


容器类型；字典 dict
    特点:
         1.可变的容器
         2.元素存放无序(以键(key)-值(value)对存放,key value的分隔符:,key唯一)
         3.关键字 dict 符号 {}
    定义：
        1.直接赋值:{key:value,...}
        2.类型转换: dict(可迭代对象)
        3.空字典: {} 或 dict()
    访问:
        1. dict变量名[key] key 不存在时报错
        2. dict.get(key,"错误提示") key 不存在时返回错误提示
        3. 访问所有key dict变量名.keys() 或 所有 value dict变量名.values()
    修改:
        1.dict变量名[old_key]  = 值  修改指定key的value
        2.dict变量名[new_key]  = 值  添加新的元素
        3.dict变量名.update({"old_key|new_key":value,..})
        4.dict变量名.clear()  dict变量名.pop(key)   del dict变量名[key]   删除元素
    遍历:
        for i in dict变量名|dict变量名.keys(：# 遍历key
        for k,v in dict变量名.items()：# 遍历元素
    查找
        Key [not] in dict变量名

set集合:1.去重存储 2.集合运算(交集，并集，差集)
    特点:
    1.可变的容器但集合内元素不可变的(只能做增减，元素值不能变)
    2.相当于只有键没有值的字典(每个元素只有一部分组成,元素唯一)
    3.元素无序的存储结构(无需访问)
    4.关键字 set  符号{}
    定义：
        1.直接赋值: {key,...}
        2.类型转换: set(可迭代对象)
        3.空集合：set()
    查找:Key[not] in dict变量名
    运算：交集 & , 并集 |  ，差集 - ，对称差集^
    修改：只能做元素的增(变量名.add(元素) 减(clear,remove,pop)

自定义函数：封装代码,提高代码的重用性
定义：
def 函数名([形参名1,形参名2,..]): #函数名命名遵守变量名命名规则
    函数体
    [return 返回值] #没有return 时，返回null
调用:
    函数名(实参1，...)