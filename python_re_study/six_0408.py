#####################################
#6.模块
#####################################

#你可以导入1个模块
import math

print (math.sqrt(16)) #=>4

#可以从module里导入一些函数
from math import ceil,floor

print (ceil(3.7)) #=>4.0
print (floor(3.7)) #=>3.0


#可以把模块里所有的函数都导出来
#注意，这里是不推荐的做法
from math import *

#模块名是可以简写的
import math as m

math.sqrt(16) == m.sqrt(16) #=>True

#你也可以测试这是这些函数是否相等
from math import sqrt
math.sqrt == m.sqrt == sqrt #=>True

#python 的模块就是普通的python文件
#你可以创建自己的模块，然后进行导入
#模块就是文件的文件名

#你可以找出模块里定义了哪些函数和属性
import math

dir(math)

#如果你有1个名为math.py的文件
#并且该文件跟你的脚本在同一文件夹下
#你导入math.py的时候你将导入自己定义的版本
#而不是导入python标准库的math模块
#这是因为本地文件夹的导入优先级高于标准库
