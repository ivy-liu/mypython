
#############
#4.函数
############

#用“def”来定义函数
def add(x,y):
    print("x is {0} and y is {1}".format(x,y))
    return x+y #用return语句来从函数中返回具体的值

#调用函数传入参数
add(5,6) #=>打印出“x is 5 and y is 6”并返回11

#另一种调用函数的方式，使用关键字参数
add(y=6,x=5)  #使用关键字参数得话，参数出现的顺序是可以随意的

#可以定义不定长的固定位置参数
#使用*加参数名的形式
#参数将被解析成元组
def varargs(*args):
    return args

#varargs(1,2,3) #=>(1,2,3)

#可以定义不定长的关键字参数
#使用*加参数名的形式
#参数将被解析成字典
def keyword_args(**kwargs):
    return kwargs
#调用一下
temp=keyword_args(big="foot",loch="ness") #=>{"big":"foot","loch":"ness"}
print("keyword_args:\n",temp.items())
#遍历字典
for key,value in temp.items():
    print (key,value)


#也可以将2种方式结合起来使用
def all_the_args(*args,**kwargs):
    print(args)
    print(kwargs)

"""
all_the_args(1,2,a=3,b=4)
prints:
(1, 2)
{'a': 3, 'b': 4}
"""

#调用函数的时候其实就是对arg/kwargs做反向操作
#使用*来展开古荡位置参数args,使用**去展开关键字参数kwargs
args=(1,2,3,4)
kwargs={"a":3,"b":4}
all_the_args(*args) #等于调用了foo(1,2,3,4)
"""
(1, 2, 3, 4)
{}
"""
all_the_args(**kwargs) #等于调用了foo(a=3,b=4)
"""
()
{'a': 3, 'b': 4}
"""
all_the_args(*args,**kwargs) #等于调用了foo(1,2,a=3,=4)
"""
(1, 2, 3, 4)
{'a': 3, 'b': 4}
"""
#你可以将函数参数里的args/kwargs传到其他函数里去
#分别使用*和**
def pass_all_the_args(*args,**kwargs):
    print("将函数参数里的args/kwargs传到其他函数里去")
    all_the_args(*args,**kwargs)
    print (varargs(*args))
    print (keyword_args(**kwargs))





#函数作用域
x=5


def set_x(num):
    #本地变量X跟全局变量X的值是不一样的，尽管同名
    x=num #=>43
    print(x) #=>43

def set_global_x(num):
    global x
    print(x) #=>5
    x=num #全局变量X现在被设为num 6
    print (x) #=>num 6

set_global_x(6)
print(x) #=>num 6

set_x(43)
print(x) #=>num 6
print("----------")

#Python has first class functions
def creat_adder(x):
    def adder(y):
        print("--1--")
        return x+y
    print("--2--")
    return adder

add_10=creat_adder(10)
temp=add_10(3) #=>13
print("add_10:",temp)
"""
--2--
--1--
add_10: 13
"""

#这里是匿名函数
(lambda x:x>2)(3) #=>True
(lambda x,y:x**2+y**2)(2,1) #=>5

temp=(lambda x,y:x**2+y**2)(2,1)
print("(lambda x,y:x**2+y**2)(2,1) =>",temp)
temp=(lambda x:x>2)(3)
print("(lambda x:x>2)(3) =>",temp)

#这是内置的高阶函数
map(add_10,[1,2,3]) #=>[11,12,13]
map(max,[1,2,3],[4,2,1]) #=>[4,2,3]

filter(lambda x:x>5,[3,4,5,6,7]) #=>[6,7]


temp_01=map(add_10,[1,2,3])
temp_02=map(max,[1,2,3],[4,2,1])
temp_03=filter(lambda x:x>5,[3,4,5,6,7])

print("temp_01:",str(temp_01))
print("temp_02:",str(temp_02))
print("temp_03:",str(temp_03))



#可以使用列表表达式去实现优雅的maps和filters
[add_10(i) for i in [1,2,3]] #=>[11,12,13]
[x for x in [3,4,5,6,7] if x>5] #=>[6,7]

temp_04=[add_10(i) for i in [1,2,3]]
temp_05=[x for x in [3,4,5,6,7] if x>5]
print("temp_04:",str(temp_04))
print("temp_05:",str(temp_05))

#也可以用字典表达式来构造集合和字典
{x for x in "abcdefg" if x in 'abc'}  #=>{'a', 'c', 'b'}
{x:x**2 for x in range(5)} #=>{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

temp_06={x for x in "abcdefg" if x in 'abc'} 
temp_07={x:x**2 for x in range(5)}
print("temp_06:",temp_06)
print("temp_07:",temp_07)

