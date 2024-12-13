# dict1 = {'name':'gu','age':18,'sex':'nv'}
# dict2=dict(name='gu',age=18)
# print(dict1,dict2)
#
# print(dict([['name','gu'],['age',18]]))
#
# print(dict(((1,'yi'),(2,'er'))))
#
# print(dict1['name'])
# print(dict1.get('nam1e'))
#
# print(dict1.keys())
# print(dict1.values())
from itertools import filterfalse


# str1='abcaabac'
# dict1 = {}
# for i in str1:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] = dict1[i] + 1
#
# print(dict1)

# d2={'abc':1,'def':2,'name':'fa','birth':'fksl'}
# keys = list(d2.keys())
# for i in keys:
#     if len(i) == 3:
#         del d2[i]
# print(d2)
#
# i=5
# dict1 = {}
# while i>0:
#     str1 = input('请输入姓名：')
#     float2 = float(input('请输入年龙：'))
#     if str1 not in dict1:
#         dict1[str1] = float2
#     else:
#         if dict1[str1] < float2:
#             dict1[str1] = float2
#     i=i-1
# print(dict1)
# dict1 = {'zhangsan': 10, 'lisi': 90, 'wangwu': 80, 'li': 68, 'ji': 67}
#
# for key,val in dict1.items():
#     print(key,val)

# s1= {1,2,3}
# s2={1,2,4}
# print(s1 & s2)
# print(s1 | s2)
# print(s1 - s2,s2-s1)
# print(s1 ^ s2)

#
# s1= {1,2,3}
# s1.add(7)
# s1.remove(2)
# s1.pop()
# s1.clear()
# print(s1)

# str1="deacfacb"
# s1 = set(str1)
# l1 = {}
# for i in s1:
#     l1[i] = str1.count(i)
# count_max = max(l1.values())
# list2 = list(l1.keys())
# list2.sort()
#
# for i in list2:
#     if l1[i] == count_max:
#         print(i,l1[i])
# print(list2,count_max,s1,l1)

# def test_max(num1,num2):
#     return max(num1,num2)
# print(test_max(10,1))

# def zhi_shu(num):
#     for i in range(2,num):
#         if num%i==0:
#             return  False
#     return True
#
# kaishi = 50
# while kaishi <=100:
#     if zhi_shu(kaishi):
#         print(kaishi)
#     kaishi = kaishi +1
#
# def ciao_ji(p1, p2):
#     s1 = set(p1)
#     s2 = set(p2)
#     return s1 & s2

# import random
# random1 = random.randint(0,100)
# print(random1)
# cishu=10
# while cishu >=1:
#     num1 = int(input('请输入0-100的随机数:'))
#     cishu = cishu - 1
#     if num1 == random1:
#         print('恭喜你，猜对了，随机数为',random1)
#         break
#     else:
#         print('非常遗憾，猜错了，继续努力，您还有{}次机会'.format(cishu))

# def add_dict(a,*mul_shuzi,b,**dict1):
#     he = a+b
#     for i in mul_shuzi:
#         he = i+he
#     for i in dict1:
#         he = dict1[i] + he
#     return he
#
#
#
# print(add_dict(100,200,300,b=10,f=10,e=10,c=30))
# list1 = [1,2,3,4]
# print(list(map(lambda zhi:zhi+1,list1)))
#
# l1=[1,2,3,4]
# l2=[2,5,10,11]
#
# print(list(map(lambda shu,shu2:shu+shu2,l1,l2)))

l1 = [1,2,3,4]
# l2 = [i+1 for i in l1]
l2 = [i for i in l1 if i>2]
print(l2)



