# -*- coding:utf-8 -*-
# python内置一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
"""

定义和使用列表
    - 用下标访问元素
    - 添加元素
    - 删除元素
    
"""
from collections import deque

classmates = ['Michael', 'Bob', 'Tracy']


print(len(classmates))
# 通过下标访问元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# 添加元素
classmates.append("负面情绪满满的怎么办")
print(classmates)

classmates.insert(1, "爱吃棒棒糖")
print(classmates)

# 删除元素
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)

classmates.remove('Bob')
print(classmates)

"""
列表常见操作
    - 列表连接
"""
print('列表常见操作 begin----')
# 列表连接
another = ['赵武灵王']
classmates += another
print(classmates)

# 列表切片
classmates[:2] =[0, 0]
print(classmates)

print('***********切片 being************')
print(classmates[-3:-1])

print(classmates[:])

print(classmates[::-1])

print('***********切片 end**************')

print(classmates.count(0), classmates.count('Tracy'))

classmates.insert(2, -1)
classmates.append("作妖")

print(classmates)

print(classmates.index(-1))

print(classmates.pop())

print(classmates)



print('列表常见操作 end-------')




classmates[0] = '刘备'
classmates[1]='关羽'
classmates[2]='张飞'

print(classmates)

print('stack begin -----')

classmates.append(6)
classmates.append(7)

classmates.pop()

print(classmates)

classmates.pop()
print(classmates)

print('stack end -----')


# 队列
print('queue begin -----')


queue = deque(['张三', '李四', '王二'])
queue.append('麻子')
queue.append('蛋蛋')

print(queue)
print(queue.popleft())
print(queue.popleft())

print(queue)


print('queue end -------')

# 列表生成器
print('list comprehensions begin')
# map()会根据提供的函数对指定序列做映射

# 第一个参数function以参数序列中的第一个元素调用function函数，返回包含每次function函数返回值的新列表


squares = list(map(lambda x: x**2, range(10)))
print(squares)

# 等价于
squares = [x**2 for x in range(10)]
print(squares)
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

print([x for x in vec if x >= 0])

print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry', 'passion fruit']
print([weapon.strip() for weapon in freshfruit])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# 列表推导式可使用复杂的表达式和嵌套函数

from math import pi
print([str(round(pi, i) for i in range(1, 6))])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

# zip函数用于将可迭代的对象作为对象，将对象中对应的元素打包成一个个元祖，然后返回由这些元祖组成的列表
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用*号操作符，可以将元祖解压列表
a = [1, 2, 3]
b = [4, 5, 6]
zipped = zip(a, b)
print(list(zipped))
print('list comprehensions end')

# del语句
print('del begin')
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
print('del end')




classmates[:] = []

print(classmates)

L = ['Apple', 123 , True]

s = ['python','java', ['asp', 'php', 'scheme']]

print(len(s))

print(s[2][1])

L = []

print(len(L))

# 元组 tuple tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')

print(classmates)

t = 12345, 54321, 'hello'
print(t[0])
u = t, (1, 2, 3, 4, 5)

print(u)
print(t[0])

empty = ()
singleton = ('笑嘻嘻')
print(len(empty))
print(len(singleton))
print(singleton)

# 元祖封装

x, y, z = t
print('x=', x)
print('y=', y)
print('z=', z)

t = (1)

print(t)

t = (1,)
print(t)

t = ()

print(t)

# python在现实只有1个元素的tuple时候，也加一个逗号，以免你误解数学计算上的括号

# 作业
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

"""
集合
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print(('orange' in basket))
print(('crabgrass' in basket))

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 集合推导式语法
a = {x for x in 'abracdfdfd' if x not in 'abc'}
print(a)

# 列表
fruits = ['橘子', '苹果', '香蕉', '梨', '桃子']

man = ['张三', '李四', '王二', '麻子', '张三']

# fruits.append(man)
# print(fruits)

fruits.extend(man)
print(fruits)

print(fruits.count('张三'))
print(fruits.count('自由'))

print(fruits.index('张三'))
print(fruits.index('张三', 6))

fruits.reverse()
print(fruits)

fruits.append('美丽')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop(2))

print(fruits)

# 把列表当成栈来使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)
stack.pop()
print(stack)

# 把列表当成队列使用
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('我靠')
queue.append("塔下意识粉")
print(queue)

print(queue.popleft())
print(queue.popleft())

print(queue)

# 列表推导式
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
 # map 参数： 1.函数 2， 一个或者多个序列， 前面函数的参数
print(list(map(lambda x, y: x+y, range(10), range(4))))

print('------')
print([2 * x for x in range(4)])

print([x**2 for x in range(10)])

# python list， truple, str, dict这些都是可以被迭代，但他们并不是迭代器
# 因为和迭代器相比有一个不同，这些都是大小确定。但迭代器不是，迭代器不知道要执行多少次
# 是惰性的
# 1.判断是不是可以迭代 用Iterable
# 2.判断是不是迭代器 用Iterator
# 所以凡是可以for循环的，都是可以迭代的
# 凡是可以next的，都是迭代器

# itertion 就是迭代，一个接一个，是一个通用的概念，比如一个循环遍历某个数组
# iterable 这个是可迭代对象，属于python名称，范围也很广，可重复迭代，满足如下之一都是
    # 可以for循环
    # 可以按index索引的对象，就是定义了getitem方法，比如list,str
    # 定义了__iter__方法，可以随意返回
    # 可以调用iter(obj)，并且返回iterator
# iterator 迭代器对象，也属于python名词，只能迭代一次。需要满足如下迭代器协议
    # 定义了__iter__方法，但是必须返回自身
    # 定义了__next__方法。用来返回下一个值，并且当没有数据了，抛出StopIteration可以保持当前的状态

# ------------------
# str和list是iterable 但不是iterator
print('********************************')

si = iter('Hello')
print(si)  # iter(obj)返回iterator
print(si.__iter__) # 拥有__iter__
print(si.__next__) # 包含next方法

print(si.__iter__() is si) # __iter__()返回的是自身

class DataIter(object):

    def __init__(self, *args):
        self.data = list(args)
        self.ind = 0

    def __iter__(self): #返回自身
        return self

    def __next__(self): #　返回数据
        if self.ind == len(self.data):
           raise StopIteration
        else:
           data = self.data[self.ind]
           self.ind += 1
           return data
d = DataIter(1, 2)
print(d)
for x in d:
    print(x)
# print(d.__next__())
# iterator只能迭代一次，iteraable对象则没有这个限制

class Data(object):
 
    def __init__(self, *args):
        self.data = list(args)
    
    def __iter__(self):
        return DataIterator(self)

class DataIterator(object):
    def __init__(self, data):
        self.data = data.data
        self.ind = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind == len(self.data):
            raise StopIteration
        else:
            data = self.data[self.ind]
            self.ind += 1
            return data

da = Data(1, 2, 3)
for x in da:
    print(x)
for x in da:
    print(x)
print('********************************')

# 迭代器的功能可以使用列表代替，但如果有很多值，列表就会占用太多的内存

# 对于要返回迭代器的类,要实现iterator.iter()，iterator.next()

# 迭代器对象被要求支持下面的两个方法，合起来形成迭代协议。

# iterator._iter_()

# 返回迭代器对象自身。为了允许容器和迭代器被用于for和in语句中，必须实现该方法。

# iterator._next_() 
# 返回容器的下一个条目。如果没有更多的条目，抛出StopIteration异常

# 另外需要注意的是在迭代器中next方法是return下一个元素的值

# ------------------------------------------------------------------------
# 生成器(generator) 是创建迭代器的简单而强大的工具。它们写起来就像是正规的函数，只是在需要返回数据的时候使用yield语句。每次next()被调用时，生成器会返回它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值
# 任何使用yield的函数都称之为生成器，唯一的区别在于实现方式上不一样，后者更加简洁

# 首先明确的就是生成器也是iterator迭代器，因为它遵循了迭代器协议，生成器函数跟普通的函数只有一点不一样
# 把return换成了yield，其中yield是一个语法糖，内部实现了迭代器协议，同时保持状态可以挂起
# (自动创建了__iter__()和__next__()方法，生成器显的很简洁)
# 另外一种说法：生成器就是一个返回迭代器的函数，与普通函数的区别是生成器包含yield语句，更简单点理解生成器就是一个迭代器
# 使用yield，可以让函数生成一个序列，该函数返回的对象类型是"generator"，通过该对象连续调用next方法返回序列值

def count(n):
    print('cunting')
    while n > 0:
        print('before yield')
        yield n
        print(n)
        n -= 1
        print('after yield')

# c = count(7)
# print(type(c))
# c.__next__()

# c.__next__()

# c.__next__()

for i in count(5):
    print(i)


# 还有一种定义生成器的方法：生成器表达式 类似于推导式，但是生成器返回按需产生结果的一个对象，而不是一次构建一个结构列表
# 将列表推导式的中括号换成圆括号，就是一个生成器

print(type(x for x in 'abracadabra' if x not in 'abc'))
print(list(x for x in 'abracadabra' if x not in 'abc'))
print(tuple(x for x in 'abracadabra' if x not in 'abc'))
print(set(x for x in 'abracadabra' if x not in 'abc'))

# 推导式是一个或者多个迭代器快速简洁创建数据结构的一种方法

# 列表推导式
# [expression for item in iterable]

# 加上条件表达式形式
# [expression for item x in iterable if condition]

# 多个for的嵌套表达式
# [(x, y) for x in x_list fo y in y_list]

# 字典推导式
# [key_expression:value_expression for expression in iterable]

# 集合推导式
# {expression for item in iterable}

# 生成器推导式
# 元祖没有推导式，它的圆括号是用来生成生成器推导式
# 生成器可以转化成列表推导式t_list = list(t_generotor)

# 使用zip并行迭代，zip函数在最短序列用完就会停止
# 配合ditc()函数和zip()函数的返回值可以得到一个字典. 
days= {'monday' , 'tuesday', 'wednesday'}
fruit= {'banana', 'orange', 'peach'}
dessert = {'misc', 'drink', 'ice', 'pudding'}
for day,fru,drink in zip(days,fruit,dessert):
    print(day, fru, drink)

print('***********************************')

# -------------------------------------------------------------------

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# 与下面相同
combs= [] 
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

# if表达式过滤
print([x for x in vec if x >= 0])

print([abs(x) for x in vec])

fresh = ['  自由', '民主 ', '  使命', '  黑暗']

print([weapon.strip() for weapon in fresh])
# 创建元祖列表
print([(x, x**2) for x in range(6)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([num for elem in vec for num in elem])

# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)]) 
#y以上等价于下
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 通俗点就是把几个列表(0或者1或者多个)的对应位置的元素组成新的tuple
print(list(zip(*matrix)))

# del声明
a = [-1, 1, 66.25, 333, 333, 1234]
del a[0]
print(a)
del a[0:2]
print(a)


# 元祖和序列
t = 1212, 31221, 'hello'
print(t[0])
print(t)

# 元祖是不可变的,但是它可以保护可变元素
empty = ()
singleton = 'hello',
print(len(empty))

print(singleton)

t = 12345, 54321, 'hello!'
x, y, z = t
print(x)
print(y)
print(z)

# 集合
# 集合是无序的，没有重复元素
# set()方法可以被用来产生集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

aset = set('abracadabra')
bset = set('alacazam')
# 集合还有这种操作，简直了
print(aset)
print(bset)
print(aset - bset)
print(aset | bset)
print(aset & bset)
print(aset ^ bset)

# 和列表推导式一样，集合推导式也被支持
anotherset = {x for x in 'abracadabra' if x not in 'abc'}
print(anotherset)
"""
 字典
 字典是由键索引，可以是任何不变的类型：字符串和数字永远是键
 元祖可以用作键，如果它们只包含字符串，数字或元祖
 如果元祖直接和间接包含任何可变对象，则不能将其用作键，因为列表可以使用索引分配，切片分配或者方法修改
"""
print('-----dict begin-----')
tel = {'jack' : 4098, 'sape' : 4139}
tel['guido'] = 4127
print(tel)

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))

print('guido' in tel)
print('jack' not in tel)
# dict() 方法会列表键值对中创建字典
print(dict([('空气', 4139), ('空', 32), ('大炮', 434)]))
# 字典推导式
print({x : x**2 for x in (2, 4, 6)})
# 当键是字符串的时候，可以容易的用关键字参数
print(dict(sape=4139, guido=4123, jack=4098))

"""
循环技巧
"""
knights = {'gallahad' : '明礼诚信', 'robin' : '快跑'}
for k, v in knights.items():
    print(k, v)

# 对列表循环，位置索引和相应的值可以被检索
for i, v in enumerate(['张三', '李四', '王二']):
    print(i, v)

# zip()函数同时循环多个列表，条目可以配对
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('fuck out of {0}? It is {1}'.format(q, a))

# 对序列反转函数reversed()
for i in reversed(range(1, 10, 2)):
    print(i)

# 对序列进行排序的函数
basket = ['apple', 'orange', 'apple', 'pear', 'orange']
for f in sorted(set(basket)):
    print(f)



import math
raw_data = [56.2, float('Nan'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

# 更多条件判断
# 不只是比较 in / not in 可以用来检查值是否在一个序列中，is / is not用于比较两个对象(这只对可变对象而言)
# and 和 or被称为短路操作符， 当一般值不是布尔值时候，返回的短操作符是最后一个评估参数
string1, string2, string3 = '', 'Trondheim', 'hammer Dance'
non_null = string2 and string3 
print(non_null)

# 比较序列和其他类型
print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])

print('ABC' < 'C' < 'Pascal' < 'Python')




