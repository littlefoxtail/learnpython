# -*- coding:utf-8 -*-

"""
python中的计算
"""

# 除法的话返回的类型是带小数点的
print(17 / 3)
print((60 - 5 * 6) / 4)

# 这么除放弃小数点
print(17 // 3)

# 取余数
print(17 % 3)

# 取指数
# 平方
print(5 ** 2)

print(2 ** 7)

# 多种数据进行运算，整形会转成浮点数
print(4 * 3.751 - 1)

# 虚数
print((3 + 5j) + 2)

# 绝对值
print(abs(-12 + 5))

# 转成整形
print(int(4.545 + 3.332))

# 转成浮点型
print(float(121 + 212))

# Pair (余数,)
print(divmod(2, 5))

print('---')

print(1 << 1)
print(1 << 2)
print(1 << 3)
print(1 << 4)
print(1 << 102)

flags = 1 << 2 | 1 << 3
print(flags & 1 << 2)

"""
字符串
"""
# 单引号和双引号
print('spam eggs')

print('doesn\'t')

print("doesn't")

print('"Yes," he said.')

# 引号前加r
print(r"cfd\n")

# String的多行显示,每一行行尾都会换行，\会禁用换行
print("""
i 
love
you\
""")

print('''\
i
love
her
''')

# Strings可以用+链接 *表示重复
print(3 * "fda" + 'fd')

# 字符串自动连接
print("i" ' love' ' you')

# 字符串自动连接，不能连接一个变量和一个字符串, 这个时候就得用+
var = "love"
print(var + " me")

# 拆分长字符串的话
TEXT = ('你是什么东东啊 我了个擦'
       '打包你发嗲见覅大')
print(TEXT)

# 字符索引
word = 'Python'
print(word[0])
print(word[1])

print(word[-1])
print(word[-2])

# 字符串切片 可以获取字符串
print(word[0:2])
print(word[:2])
print(word[:4] + word[4:])

# 切片都有默认值 省略值其实 0, size
print(word[-2:5])

# 切片的工作方式：切片时的索引是在两个字符之间。左边第一个字符的索引是0，而长度为n的字符串最后一个字符的右索引为n
# 我怎么感觉也可以取头部取尾来记忆呢

# 对于非负索引，如果上下都在边界内，切片的长度就是两个索引只差

# 试图太大的索引会导致错误，但python能够优雅地处理那些没有意义的切片索引
print('----')
print(word[4:42])

print(word[42:])

# 咋记忆索引
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 

# String中字符串是不可变得，更改string会报错

# len方法可以返回字符串的长度
print(len(word))

print(word[-1:])

'''
Python有几个复合数据类型，用于表示其它的值。
List是一系列复合类型的数据类型中最通用的一种，用逗号分隔， List可以包含多种类型，但通常都用一种类型
'''

squares = [1, 4, 9, 16, 25]
print(squares)

# 集合和字符串一样，可以被索引和切片
print(squares[1])

print(squares[:4])

#切片操作，返回一个新的列表，也可以返回一个浅拷贝
print(squares[:])

# 列表同样支持连接 +
print(squares + [3429, 32, 32])

# 和字符串不一样，列表是可变的，可以改变他们的内容
cubes = [1, 8, 27, 65, 125]
cubes[3] = 54
print(cubes)

# 也可以添加新的项目
cubes.append(4343)
print(cubes)

# 列表的切片,还可以更改列表大小和清空
print("改变列表大小和清空")
cubes[:] = [1, 2, 3, 4]
print(cubes)

cubes[2:5] = [6, 7, 8]

print(cubes)

cubes[2:5] = []
print(cubes)

# 内建函数len同样适用列表
letters = ['a', 'b', 'c', 'd']
print(len(letters))


# 列表还可以嵌套
a = ['a', 'b', 'c']
n = ['1', '2', '3']
x = [1, 2, 3]
print([a, n])
print([a, n][0][1])

a, b = 0, 1 
while b < 100:
    print(b, end=',')
    a, b = b, a+b

