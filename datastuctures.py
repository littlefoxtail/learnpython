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

# 字典
# 字典是由键索引，可以是任何不变的类型：字符串和数字永远是键
# 元祖可以用作键，如果它们只包含字符串，数字或元祖
# 如果元祖直接和间接包含任何可变对象，则不能将其用作键，因为列表可以使用索引分配，切片分配或者方法修改

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

# 循环技艺
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

print('ABC' < 'C' < 'Pascal' > 'Python')


