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

# 显示内建函数和变量，这些被定义在builtins中：
import builtins
print(dir(builtins))

# package是通过使用“虚线模块名称”来构造Python模块名称空间的一种方法。
# 当导入包，python会在sys.path中寻找子目录名
# 需要使用__init__.py文件来使Pyton将目录视为包含包；这是为了防止具有通用名称的目录无意中隐藏在模块搜索路径中发生的有效模块后面
# 意思有__init__.py先搜索  流弊不流弊
import apply.packageexample.package

# load的话得全称
apply.packageexample.package.echofilter()

# 替代的导入方法
from apply.packageexample import package
package.echofilter()

# 也可以这样哦
from apply.packageexample.package import echofilter
echofilter()

# 注意在使用 from package import item时候，item可以是是子模块，也可以是包中定义的方法，类和变量
# 相反的，当使用import item.subitem.subsubitem 最后一个必须是一个module或者package 不能是一个方法









