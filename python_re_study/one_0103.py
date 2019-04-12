
##########################################
# 1.基本数据类型及操作
# ###########################################





#以..#..开头进行单行注释
"""
使用3个双引号
来定义多行文本
多行文本一般用来
做文档注释
"""
#这是数字
3  #=>3

#这是做简单的算术
1+1  #=>2
6-2  #=>4
10*2 #=>20
35/5 #=>7

#python2除法默认做整数除法，舍去余数
#pyrhon3除法做普通除法,如下
5/2 #=>2.5
e=5/2
print("e=",e)

#我们一般所认知的除法在python里其实就是浮点数除法
2.0 #浮点数float
11.0/4.0 #=>2.75

#可以强制返回整数，整数负数都可以
5//3 #=>1
5.0//3.0 #=>1.0
a=5//3
b=5.0//3.0
print("a=",a)
print("b=",b)

-5//3 #=>1
-5.0//3.0 #=>-2.0
c=-5//3 
d=-5.0//3.0 
print("c=",c)
print("d=",d)

'''
注意，python2我们可以用import division 模块
这样'/'就可以实现普通的我们熟悉的除法功能了
python3里面'/'默认就是普通除法模式了
from __future__ import division
'''

#模/取余操作
7%3 #=>1
#乘方（x的y次方）
2 ** 4 #=>8
#用括号改变算术的结合律
(1+3)*2 #=>8

#布尔值操作或者叫做逻辑运算
# and 和 or 区分大小写
True and False #=>false
False or True #=>true
print("True and False=",True and False)
print("False or True=",False or True)

#布尔值和整数
0 and 2 #=>0
-5 or 0 #=>-5
-5 and 0 #=>0
print("0 and 2 = ",0 and 2)
print("-5 or 0 = ",-5 or 0)
print("-5 and 0 = ",-5 and 0)

0==False #=>true
2==True #=>false
1==True #=>true
print("2==True:",2==True)

#用not来逻辑取反
not True #=>flase
not False #=>true
print("not True:",not True)
print("not False:",not False)

#相等判断用==
1==1 #=>true
2==1 #=>flase

#不等用！=
1!=1 #=>false
2!=1 #=>true

#更多得比较
1<10 #=>true
1>10 #=>false
2<=2 #=>true
2>=2 #=>true

#比较可以串起来
1<2<3 #=>true
2<3<2 #=>false

#用"或'来创建字符串
"this is a string ."
'this is also a string.'

#字符串相加
"hello"+"world!" #=>"hello world!"
g="hello,"+"world!"
print("g=",g)
#不用加号也能相加
"hello" "world!" #=>"hello world!"
f="hello," "world!" 
print("f=",f)

#字符串相乘
"hello"*3 #=>hellohellohello
h="hello"*3
print("h=",h)

#字符串可以当作字符组成的列表
"this is a string"[0] #=>'t'
print("this is a string"[0])

#拿到字符串的长度
len("this is a string") #=>16
length=len("this is a string")
print("length=",length)

#可以用 % 来格式化字符串
#even though the % string operator will be deprecated on python3.1 and removed
#即使知道%操作在python3.1以后会被废弃和移除
#不过知道这些代码是怎么工作的不是坏事情

i='apple'
j='lemon'
k="the item in the basket are %s and %s" % (i,j)
print("k: ",k)
#现执行python3.6.5仍可以使用

#新一点的格式化字符串的方式是使用format方法
#这个方法更好一些？？
"{} is a {}".format("this","placeholder")
"{0} can be {1}".format("strings","formatted")
#不想数数，可以使用关键字
"{name} wants to eat {food}".format(name="bob",food="lasagna")

l="{} is a {}".format("this","placeholder")
m="{0} can be {1}".format("strings","formatted")
n="{name} wants to eat {food}".format(name="bob",food="lasagna")
print("l:",l)
print("m:",m)
print("n:",n)


#None是一个对象
#所以你是有对象的
None #=>None

#不要使用"=="服号及逆行对象和 None 的比较
#要使用"is"
"etc" is None #=>false
None is None #=>true
o="etc" is None
p=None is None
print("o:",o)
print("p:",p)

'''
'is'符号用来测试对象的之间的相当性
在比较基本类型的时候用处不大
不过在对象的比较方面却是很有用的
'''


'''
any object can be used in a boolean context
任何的对象都可以在布尔值的上下文中使用
下面的值会被认为是false
    -None
    -zero of any numeric type (e.g.,0,0L，0.0，0j)
    -任何数字类型的0（比如，0,0L，0.0，0j）
    -空序列（比如，''，()，[]）
    -空的容器类型（比如，{}，set()）
    -某些情况下用户自定义的类的实例
    见：https://docs.python.org/2/reference/datamodel.html#object.__nonzero__

其他的值都被认为是true(使用bool()测试这些值的时候会返回true).
'''
bool(0) #=>false
bool("") #=>false












