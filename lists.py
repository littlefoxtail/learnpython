'''
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
cubes[:] = [1, 2, 3, 4]
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

