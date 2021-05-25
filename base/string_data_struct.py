
import sys
#string
#def println():
#    print('\n')

def println(str=''):
    print(str)
    print('\n')

def printDivider():
    divider = ''
    println(divider.rjust(100, '#'))

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
println()
s1 = 'hello'* 3
print(s1)
s2 = 'world'
println()
s1 += s2
print(s1)
println()
print('ll' in s1)
println()
print('good' in s1)
println()

printDivider()

str = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str[2]) #c
# 字符串切片(从指定的开始索引到指定的结束索引)
println()
print(str[2:]) #c123456
println()
print(str[2:5]) #c12
println()
print(str[2::2])  #c246
println()
print(str[::2]) #ac246
println()
print(str[::-1]) #654321cba
println()
print(str[-3::-1]) #4321cba

printDivider()

str1 = 'hello world!'
# 通过内置函数len计算字符串的长度
println('len=%d'% len(str1))
# 获得字符串首字母大写的拷贝
println('capitalize=%s' % str1.capitalize())
# 获得字符串每个单词首字母大写的拷贝
println('title=%s'% str1.title())
# 获得字符串变大写后的拷贝
println(str1.upper())
# 从字符串中查找子串所在位置
println(str1.find('or'))
println(str1.find('shit'))
# 与find类似但找不到子串时会引发异常
#println(str1.index('or'))
#println(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
println(str1.startswith('He'))
println(str1.startswith('hel'))
# 检查字符串是否以指定的字符串结尾
println(str1.endswith('!'))
# 将字符串以指定的宽度居中并在两侧填充指定的字符
println(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
println(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
println('isdigit=%r' % str2.isdigit())
# 检查字符串是否以字母构成
println('isalpha=%r' % str2.isalpha())
# 检查字符串是否以数字和字母构成
println('isalnum=%r' % str2.isalnum())
str3 = '  popmain@gmail.com'
println(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
println(str3.strip())
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))

printDivider()

#list 中扩号
list1 = [1, 2, 3, 4, 5, 6]

println(list1)

list2 = ['hello'] * 3

println(list2)

println(len(list1))

println(list1[0])

println(list1[-1])

println(list1[-3])

list1[2] = 300

println(list1)

for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)

for index, elem in enumerate(list1):
    print(index, elem)


printDivider()

list1 = [1,3,5, 7,100]

list1.append(200)
list1.insert(1, 400)
print(list1)

list1 += [10000, 20000]

print(list1)

if 3 in list1:
    list1.remove(3)

if 1234 in list1:
    list1.remove(1234)

print(list1)

list1.pop(0)
print(list1)

list1.pop(len(list1) - 1)
print(list1)

list1.clear()
print(list1)

printDivider()

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)

fruits4 = fruits[-3:-1]
print(fruits4)

fruits5 = fruits[::-1]
print(fruits5)

printDivider()

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

printDivider()

#生成式和生成器

f =[x for x in range(1, 10)] 
println(f)

f = [x + y for x in 'ABCD' for y in '1234']

println(f)
# 数组
f = [x ** 2 for x in  range(1, 1000)]
println(sys.getsizeof(f))
println(f[0])
#println(f)
#生成器
f = (x ** 2 for x in range(1, 100))
println(sys.getsizeof(f))
# println(f[0])TypeError: 'generator' object is not subscriptable
#println(f)
#for val in f:
#    println(val)

#yield

def fib(n):
    a, b = 0, 1
    for _ in range(n):
           a,b=b, a+b
           yield a
for val in fib(20):
    println(val)


#tuple 括号
t = ('骆昊', 38, True, '四川成都')

#t[0] = 3333 错误，tuple不能修改

println(t)

t = ['骆昊', 38, True, '四川成都']

println(t)

#set 花括号
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
printDivider()
print(set1, set2)
printDivider()
print(set3.pop())
printDivider()
println(set3)

set1 = {1, 2, 3, 4, 5}
set2 = {2,4,6,7}
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

#dictionary 或括号 {key:value}

d = {1: 'a', 2:'b', 3:'c'}
println(d[1])
d[1] = 'w'
d.update({4:'d', 5:'e'})
println(d.get(4))
println(d)
d.popitem()
d.popitem()
d.pop(1)
println(d)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
println(items1)

# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
println(items2)
# 创建字典的推导式语法
item3 = {num: num ** 2 for num in range(1, 10)}
println(item3)
