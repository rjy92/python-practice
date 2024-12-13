# 1.随意定义个列表l1，一个元组t1
l1=[1,2,3,"a",'b',"c"]
t1=(1,2,"a","d")
# 2.找出l1,t1的共同存在元素
print(set(l1) & set(t1))
# 3.计算l1,t1两个容器的去重后元素个数
print(len(set(l1) | set(t1)))
# 4.定义一个集合s1,定义一个与s1等长度的列表l2, 创建一个空字典d1，
# 把s1元素作为key l2元素作为值放入到d1中
s1={1,2,"a","b"}
l2=["v1","v2",100,10]
d1={}
l2_index=0
for i in s1:
  d1[i] = l2[l2_index]
  l2_index = l2_index+1
print(d1)

# 5.自定义函数实现 容器对象的len功能
def test_len(rongqi):
  count=0
  for i in rongqi:
    count=count+1
  return count
print(test_len([1,2]),
      test_len(("a",1,3)),
      test_len({1,2,3}),
      test_len({1:"a"}))
# 6.随机生成一个100以内的整数，给10次机会让用户猜
# import random
# random1 = random.randint(0,100) #随机生成一个100以内的整数
# #   #实现最多10次猜字游戏
# cishu = 10
# while cishu>=1:
#   zhi = int(input("请猜100以内的整数"))
#   if zhi==random1:
#     print("你猜对了，随机数为{}，你猜的为{}".format(random1,zhi))
#     break
#   cishu=cishu-1
#   if zhi > random1:
#     print("你猜大了，你还有{}次机会".format(cishu))
#   else:
#     print("你猜小了，你还有{}次机会".format(cishu))

调用函数的传参方式
1.位置传递参数，2.关键字传参

def add_test(zhi1,zhi2): #zhi1,zhi2 形参：只是定义一个名字具体内容调用时才知道
  print("zhi1的值是",zhi1)
  print("zhi2的值是", zhi2)
  return zhi1+zhi2

add_test(1,2) #位置传递参数  #参数叫实参：有实际的具体的值了
add_test(zhi2=200,zhi1=100)#关键字传参

形参定义方法
1.位置形参
2.函数的缺省参数
def add_test(zhi1,zhi2=200): #部分形参有默认值
  print("zhi1的值是",zhi1)
  print("zhi2的值是", zhi2)
  return zhi1+zhi2
print(add_test(1,2),add_test(1))

3.星号元组形参(*args)  #参数数量不定时使用
def add_mul(*mul_zhi): #求任意多个数值的和
  #mul_zhi是一个元组 (把对应位置后的所有值放到元组中)
  he=0
  for i in mul_zhi:
    he = he +i
  return he
print(add_mul(100,200,300,200,500),
      add_mul(1,2),
      add_mul(1),
      add_mul(3,4))
4.命名关键字形参:当*元组后还有形参，传参时一定要指定参数名
def add_key(a,*mul_zhi,b):
  he =a+b
  for i  in mul_zhi:
    he = he+i
  return he
print(add_key(10,20,30,40,b=50))

5.双星号字典形参(**kwargs)：出现在形参的最后，只能有一个
def add_dict(a,*mul_zhi,b,**dict1):
  he =a+b
  for i  in mul_zhi:
    he = he+i
  for i in dict1:
    he =he+ dict1[i]
  return he
print(add_dict(10,20,30,b=50,c=10,d=20,e=50))



局部变量:只能在函数内使用的变量(函数内定义的变量,函数的形参)
def add_test(zhi1,zhi2): #zhi1,zhi2 形参：只是定义一个名字具体内容调用时才知道
  he = zhi1 + zhi2
  print(he)
  return he
add_test(1,2)

全局变量:在整个文件中都能使用的变量
a=10
b=20
def add_test():
  he = a+b #函数内可以访问全局变量,不能改
  print(he)
add_test()

he = 10
def add_test(zhi1):
  global he #声明 he 为全局变量
  c = he+zhi1
  he=c #改全局变量，提前声明是全局变量
  print(c) #20
add_test(10)
print(he)

python 自定义函数（1.def  2.lambda )
函数体只有一句话 匿名函数lambda

def add_test(zhi1,zhi2):
  return zhi1+zhi2
匿名==没名== 声明完无法使用 ——与其他函数共同使用 map
map(函数,第一个函数的参数值_可迭代对象,...) #把可迭代对象里的每个元素给函数进行执行
lambda 形参:一句函数体
l1=[1,2,3,4] #为l1 每个元素加1
l2=[]
for i in l1: #循环
  l2.append(i+1)
print(l1,l2)

l1=[1,2,3,4]
def add_1(zhi): #map + def 自定义函数
  return zhi+1
print(list(map(add_1,l1)))  #15回来

print(list(map(lambda zhi:zhi+1,l1))) #map + 匿名函数

l1=[1,2,3,4] #为l1 每个元素加1
l2=[2,5,10,11] #l1,l2 对应的元素求和、
i=0
l3=[]
while i<len(l1):
  l3.append(l1[i]+l2[i])
  i=i+1
print(l3)

def add_test(zhi1,zhi2):
  return zhi1+zhi2
print(list(map(add_test,l1,l2)))

print(list(map(lambda zhi1,zhi2:zhi1+zhi2,l1,l2)))

列表推导式:快速产生一个列表
l1=[1,2,3,4]  #1. 为每个元素加1, 2.筛选大于2的元素
l2=[]
for i in l1:
  l2.append(i+1)
print(l2)



1:加工每个元素   [表达式 for i in 可迭代对象]
l1=[1,2,3,4]
l2=[i+1 for i in l1]
print(l2)
#2.筛选元素 [表达式 for i in 可迭代对象 if 条件]
l1=[1,2,3,4]  #1. 为每个元素加1, 2.筛选大于2的元素
l2=[]
for i in l1:
  if i>2:
    l2.append(i)
print(l2)

l1=[1,2,3,4]
l2 = [i for i in l1 if i>2]
print(l2)

模块：支持从逻辑上组织Python代码
1 标准库模块(会在安装python的时候直接被安装)
2 第三方模块(需要另外安装)
 1.  pycharm里安装
  file菜单——setings——左侧 project pythonproject下的第一个选项——右侧左上角+
  搜索 yagmail (关于发送邮件的第三方模块) 后install package 按钮实现安装
 2.  命令行 pip 安装
  任务栏搜索按钮，搜索命令提示符， 输入如下指令:
  pip install 模块名 [-i 模块库网址]

3 自定义模块(是其他使用者的第三方模块)

使用模块(一个.py文件） 使用文件里的一些方法 import 模块名 [as 模块别名]
import random as rd



