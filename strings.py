# -*- coding: utf-8 -*-
"""
python中的字符串
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

# 不能连接一个变量和一个字符串, 这个时候就得用+
var = "love"
print(var + " me")

# 拆分长字符串的话
TEXT = (u'你是什么东东啊 我了个擦'
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

# String中字符串是不可变得