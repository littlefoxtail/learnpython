# 模块
import fibo
import sys
fibo.fib(1000)

print(fibo.fib2(100))


# 模块搜索路径
# 解释器先搜索该名称的内置模块，如果没有找到则会在sys.path中寻找
# 1. 包含输入脚本的目录，当前目录
# 2.
# print(sys.path)

# 标准模块(standard modules)
sys.path.append('/ufs/guido/lib/python')
print(sys.path)

import sys
print(dir(fibo))

print(dir())



