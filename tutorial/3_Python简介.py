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
print(word[1])

# 字符串切片 可以获取字符串
print(word[0:2])
print(word[:2])
print(word[:4] + word[4:])

# 切片都有默认值 省略值其实 0, size
print(word[-2:5])

# 咋记忆索引
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 

# String中字符串是不可变得，更改string会报错

# len方法可以返回字符串的长度
print(len(word))

