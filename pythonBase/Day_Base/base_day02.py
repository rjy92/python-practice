# 比较运算符：构造条件
# > >= < <=, 等于 ==  ,不等于 !=  结果为bool(True,False)
var1 = 2
var2 = "2"
print(var1==var2,var1!=var2)

# 逻辑(布尔)运算：多条件组合 并且关系(and) 或者关系(or) 取反(not)
# 并且关系（and) :两个条件同时满足时结果才为True
# 或者关系（or)：任一条件满足时结果就为True
var1 = 10
var2 = 8
print(var1!=var2 and var1<var2)
print(var1==var2 or var1>var2)
print(not var1>var2)

# python 的假值对象
# False,0,0.0,"",None 空对象,空容器
print(bool(0),bool(0.0),bool(""),bool(None),bool(0.0001),bool(" "))

#控制语句(条件语句if, 循环语句)
# 条件语句if语法:
# if 条件1: #在条件1下缩进的语句都受条件1 控制
#     条件1满足时语句1
#     条件1满足时语句2
#     ...
# elif 条件2:
#     条件2满足时语句1
#     条件2满足时语句2
#     ...
# ....
# else:
#     以上条件均不满足时语句1
#     ..
var1 = 9
if var1%2==0:
    print("偶数")
else:
    print("奇数")

print("if完成")
#二分支:if else, 多分支: if elif ..  else
age=21
#age= 25  #老中青  青<=24 中25-45 老>45
if age<=24:
    print("青年")
elif age>=25 and age<=45: #age<=45
    print("中年")
else:
    print("老年")

#if 可嵌套(条件语句里再写if)
age = 25
if age<=24:
    print("青年")
else:
    if age<=45:
        print("中年")
    else:
        print("老年")

score=70
# 根据分数输出分数段 不及格(<60) 及格([60,69]) 中([70,79])
# 良([80,89]) 优([90,100]) #if elif  else
result=""
if score<60:
    result="不及格"
elif score<=69:
    result="及格"
elif score<=79:
    result="中"
elif score<=89:
    result="良"
else:
    result="优"
print(result)

# 循环语句: 控制某些代码重复执行(while,for),可嵌套
# 基本的while语法
# while 循环条件:
#     要重复执行的内容
# [else:
#     循环正常结束时执行的内容]
# 打印10次 hello world

cishu = 1
while cishu<=10:
    print("hello world")
    cishu=cishu+1
else:
    print("我打印完了")

rows=int(input("请输入打印行数"))
print_row =1
while print_row<=rows:
    print("这是第"+ str(print_row) +"行")
    print_row= print_row+1

# 打印1-20,每5个换行 while + if  %5=0  print(内容,end=)
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20

i=1
while i<=20:
    if i%5 != 0:
        print(i,end=" ")  #打印完i后,输出一个空格
    else:
        print(i)#默认end="\n"
    i=i+1

# 打印1-100的奇数,每行打印5个
# 1 3 5 7 9
# 11 13 15 17 19
# ..
# ..

i=1 #记录是100中的数值
print_i = 1 #记录打印的第几个
while i<=100:
    if i%2==1: #1-100中奇数
        if print_i %5 != 0: #一行不到5个数 空格打印
            print(i,end=" ")
        else: #一行到5个数打印后换行
            print(i) #end 默认为换行
        print_i = print_i+1 #记录开始打印第几个
    i=i+1

i=1
while i<=100:
    if i%5 != 4:
        print(i,end=" ")
    else: #i%5==4 换行
        print(i)
    i=i+2

# 99乘法表
# 外层循环控制行,内层循环控制几列
row =1
while row<=9: #1~9行
    column=1
    while column<=row: #1~row 列
        print("{}*{}={}".format(row,column,row*column),end=" ")
        #打印完每个公式后空格
        column = column+1 #下一列
    print("") #打印完一行后换行(打印个空,打印完后输出end的默认值换行)
    row=row+1 #下一行
# 1*1
# 2*1 2*2
# 3*1 3*2 3*3
# 4*1 4*2 4*3 4*4
# ...
# 9*1 9*2 9*3 9*4..... 9*9

# for: 用来遍历可迭代对象的数据元素
# 遍历:遍历是指经历且只经历一遍
# 可迭代对象:是指能够依次获取数据元素的对象
# for 变量名 in 可迭代对象:
#     循环体
# [else:
#     循环正常结束后执行的内容]

str1="abc124"
for i in str1: #有挨个获取元素功能,并且把值给变量i
    print(i)

str1="abcadeal"
#实现str1.count("a") 功能, 查看str1中有几个a
count = 0
for i in str1:
    if i=="a":
        count=count+1
print(count)

# 写一个程序，输入一个任意长度的字符串，
# 用for 语句找出这个字符串中有几个英文的等号(=)
# 如: 请输入: a = b = c = 100
#    结果: 3

str1 = input("请输入一个字符串")
count=0
for i in str1:
    if i=="=":
        count=count+1
print("=的个数",count)

# range:构造一个数值区间,为可迭代对象
# range(结束值) #0~结束值-1,步长为1
# print(list(range(5)))
# range(开始值,结束值)
# print(list(range(1,6))) #开始值~结束值-1 步长为1
# range(开始值,结束值,步长)
# print(list(range(1,10,2))) #开始值~结束值-1 步长为2

#for 循环打印
# 1
# 2
# 3
# 4
# 5
for i in range(1,6):
    print(i)

# 用for 循环1~20的打印,并且每行5个值,值与值之间用空格间隔
# 1 2 3 4 5
# 6 7 8 9 10
# ...
# 16 17 18 19 20

for i in range(1,21):
    if i%5 != 0:
        print(i,end=" ")
    else:
        print(i)

# range + for  , while  通过位置来做循环了
str1="abcabdaa" #a 的个数
#str1[0] =="a" str1[1]=="a",, str1[位置]
count=0
for i in range(len(str1)):
    if str1[i] == "a":
        count=count+1
print(count)

str1="abcabdaa" #a 的个数
start_index =0
count=0
while start_index <len(str1):
    if str1[start_index] == "a":
        count=count+1
    start_index = start_index+1
print(count)

# 输出4行,每行输出行号乘以1~10
# 一层循环控制行,一层循环控制列
for i in range(1,5):
    for j in range(1,11): #循环结束,打印完成一行
        print(i*j,end=" ")
    else:
        print("") #打印完空后,打印end的默认值 换行
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40

# del: 删除变量, 释放空间
# del 变量名[,变量名2,...]
str1 = "abc"
print(str1)
del str1
print(str1)

# 比较运算符 等于 ==  不等于 !=,
# bool运算符 条件1 and 条件2, 条件1 or 条件2, not 条件
# 控制语句
#   1 条件语句 if
#         if 条件1:
#             条件1满足时执行
#         [elif 条件2:
#             条件2满足时执行
#         .....]
#         [else:
#             以上条件均不满时足执行]
#   2 循环语句
#      while 循环条件:
#          循环体
#          构造结束条件(没有此句会造成四死循环)
#      else:
#           循环正常结束时执行
#      range 构造数值区间 range([开始值,]结束值[,步长])
#      for 变量名 in 可迭代对象_能够按个获取元素内容:
#          循环体
#      else:
#          循环正常结束时执行
#   del 变量名  删除指定的变量










