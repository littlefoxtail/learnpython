

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

* [Python](#python)
	* [Python简介](#python简介)
	* [深入Python流程控制](#深入python流程控制)
	* [数据结构](#数据结构)
	* [模块与函数](#模块与函数)
		* [函数](#函数)

<!-- /code_chunk_output -->

# Python

Python是一门解释型语言，因为无需编译和链接，可以在程序开发中节省宝贵的时间。
Python让程序编写的紧凑和可读。用Python编写的程序通常比同样的C、C++或者Java程序更短小，这是因为以下几个原因

- 高级数据结构使你可以在一条语句中表达复杂的操作
- 语句组使用缩进代替开始和技术大括号来组织
- 变量或参数无需声明

## Python简介

[Python简介](tutorial/3_Python简介.md)<br/>
[简介示例代码](tutorial/3_Python简介.py)<br/>

## 深入Python流程控制

[流程控制](tutorial/4_深入Python流程控制.md)<br/>
[流程控制示例代码](tutorial/4_深入Python流程控制.py)<br>

## 数据结构

[数据结构](tutorial/5_数据结构.md)</br>
[数据结构示例代码](tutorial/5_数据结构.py)</br>

## 模块与函数

[模块与函数](tutorial/6_模块.md)</br>
[模块与函数示例代码](tutorial/6_模块.py)</br>

### 函数

关键字`def`(defined)引入一个函数定义。在其后必须跟函数名和包括形式参数的圆括号。函数体语句从下一行开始，必须是缩进的

函数体第一行可是是可选的字符串文本，这个字符串是函数的文档字符串，或者成为docstring

函数调用会为函数局部变量生成一个新的符号表。所有函数中的变量赋值都是将值存储在局部符号表。变量引用首先在局部符号表中查找，然后是包含函数的局部符号表，然后是全局符号表，最后是内置名字表。因此，全局变量不能再函数中直接赋值(除非用`global`语句命名)，尽管他们可以被引用

函数引用的实际参数在函数调用时引入局部符号表

一个函数定义会在当前符号表内引入函数名。函数名指代的值有一个被Python解释器认定为用户自定义函数的类型。这个值可以赋予其他的名字，然后它也可以被当做函数使用。这可以作为通用的重命名机制

- return 语句从函数中返回一个值，不带表达式的return 返回`None`。过程结束也会返回`None`
- 方法是一个“属于”某个对象的函数

[计算](calculator.py)</br>
[字符串](strings.py)</br>
[列表](lists.py)</br>
[控制流工具](controlflowtools.py)</br>
[数据结构](datastructures.py)</br>
[模式](modules.py)</br>
[输入和输出](inputandoutput.py)</br>