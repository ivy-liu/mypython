
########################
# 2.变量和集合
# ######################




# # python 有 print 语句
print("I'm Python.Nice to meet you!") #I'm Python. Nice to meet you!
#python3应该这么写

#从控制台获取输入的简便方法
input_var=input("Enter some data:")
print("输入内容如下：{}".format(input_var))

#给变量赋值前不需要声明
some_var=5 #一般约定下使用下划线去给变量名分词 lower_case_with_underscores
some_var  #=>5

#访问灭有定义的变量会抛出异常
#声明即需要赋值
#在访问流部分，可以查看更多关于异常处理的信息

#
# some_other_var  
#

#if可以作为表达式使用
#跟C语言中'?:'三元操作符等价
"yahoo!" if  3>2 else 2 #=>"yahoo!"

li=[]
#你可以定义一个预填充（或者叫非空的列表可能比较好）列表
other_li=[4,5,6]

#使用append方法项列表的尾部添加元素
li.append(1) #li is now [1]
li.append(2) #li is now [1,2]
li.append(4)
li.append(3) #li is now [1,2,4,3]
#使用pop将元素从列表尾部移除
li.pop() #=>3 and li is now [1,2,4]
li.pop() #=>4 and li is now [1,2]

print("now li is:",li)

#访问列表元素和访问数组元素得预发是相同的
li[0] #=>1

#使用 = 可以给已经初始化过的索引赋新值
li[0]=23 #=>23 and li is now [23,2]
li[0]=1
print("li第一个值：",li[0])
#访问最后1个元素
li[-1] #=>3
print("li的最后1个值：",li[-1])

#访问越界的话会抛出IndexError
#li[4] #raises an IndexError

li.append(4)
li.append(3)
print("now li is:",li)
#=>li is now [1,2,4,3]

#使用切片 slice 语法可以访问列表中的部分元素
li[1:3] #=>[2,4]
print("li[1:3]:",li[1:3])
#从位置1开始到位置3结束，包括开头，不包括结尾

li[:3] #=>[1, 2, 4]
print("li[:3]:",li[:3])
#到位置3结束

li[2:] #=>[4,3]
print("li[2:]:",li[2:])
#从位置2开始

li[::2] #=>[1, 4]
print("li[::2]:",li[::2])
#每2个元素取1个

li[::-1] #=>[3, 4, 2, 1]
print("li[::-1]:",li[::-1])
#反转列表的拷贝

#use any conbination of these to make advanced slice
#使用上述的各种组合来创建更加复杂的切片
#list[start:end:step]


#使用 del 来删除元素
del li[2] #li is now [1,2,3]

#列表可以相加
li + other_li #=>[1, 2, 3, 4, 5, 6]
print("li + other_li:",li + other_li)

#使用extend()来链接字符串
#注意li的值发生变化
li.extend(other_li)  #=>now li is [1, 2, 3, 4, 5, 6]
print("now li is:",li)

#移除第一个满足条件的值
li.remove(2) #=>[1, 3, 4, 5, 6]
print("now li is:",li)
#移除 li 中 2

#li.remove(7) #抛出ValueError,因为7不在 li 中

#用 in 检查元素是否在列表中存在
1 in li #=>True
print("1 in li :",1 in li )

#用 len() 来返回列表的长度
len(li) 
print("li's length:",len(li) )

#元组（tuples）跟列表很像，区别是元组不可变
tup=(1,2,3)
tup[0] #=>1
#tup[0]=3 #抛出TypeError异常

#可以在元组上做以下这些操作
len(tup) #=>3
tup+(4,5,6) #=>(1,2,3,4,5,6)
tup[:2] #=>(1,2)
2 in tup #=>true

#you can unpack tuples (or lists) into variales
# 你可以把元组（或列表）unpack成变量
a,b,c=(1,2,3) #a is now 1,b is now 2,c is now 3
d,e,f=4,5,6 #可以省略括号
#如果不加括号，默认会创建元组
g=4,5,6 #=>(4,5,6)
#交换变量的值
e,d=d,e #d is now 5 and e is now 4

#字典是用来存储属性名（key）和属性值（value)的
empty_dict={} #这是预填充的字典
filled_dict={"one":1,"two":2,"three":3}

#用[]来查找属性的值（value）
filled_dict["one"] #=>1

#用"keys()"来返回所有key的列表
filled_dict.keys() #=>["three","two","one"]
#注意字典key的顺序是不保证的

#用"values()"返回所有value的列表
filled_dict.values() #=>[3,2,1]

#用"items()"返回所有键值（key-value）对的元组组成的列表
filled_dict.items() 
print(filled_dict.items()) #=>dict_items([('one', 1), ('two', 2), ('three', 3)])

#用"in"来判断某个属性名/某个键是否存在
"one" in filled_dict #=>true
1 in filled_dict #=>false
print("1 in filled_dict:",1 in filled_dict)

#访问不存在的属性名/键的时候会抛出KeyError
#filled_dict["four"] #KeyError

#用"get()"方法可以避免KeyError
filled_dict.get("one") #=>1
filled_dict.get("four") #=>None
#get支持当属性名/键不存在的时候返回1个设定的默认值
filled_dict.get("one",4) #=>1
filled_dict.get("four",4) #=>4
print("filled_dict.get('four',4):",filled_dict.get("four",4))
#注意，filled_dict.get("four")仍然是None，get并不会设置字典的值

#为某个属性名/键赋值跟列表赋值的方式差不多
filled_dict["four"]=4 #now
#"setdefaul()"方法在给定的属性名/键不存在的时候会插入具体的值
filled_dict.setdefault("five",5) #filled_dict["five"]被设置为5
filled_dict.setdefault("five",6) #filled_dict["five"]依然为5
print("now filled_dict is:",filled_dict)

#集合是存储。。好吧，集合（跟列表差不多，只是不能有重复的项）
empty_set=set()
#初始化的时候赋值
some_set=set([1,2,3,4])
#some_set现在等于set([1,2,3,4])

#顺序是不被保证的，即使有时候看起来像排过序一样
another_set=set([4,3,2,1])
#another_set现在也等于set([1,2,3,4])

#从python 2.7开始，{}可以被用来声明集合
filled_set={1,2,2,3,4}  #=>{1,2,3,4}

#往集合里添加更多项
filled_set.add(5) #=>filled_set is now {1,2,3,4,5}

#用 & 来取交集
other_set={3,4,5,6}
filled_set & other_set #=>{3,4,5}
print("filled_set & other_set:",filled_set & other_set)

#用 | 来取并集
filled_set | other_set #=>{1,2,3,4,5,6}
print("filled_set | other_set:",filled_set | other_set)

#用 - 来取差集
{1,2,3,4} - {2,3,5} #=>{1,4}
print("filled_set - other_set:",filled_set - other_set)

#用 ^ 取对称差集
{1,2,3,4} ^ {2,3,4,5}
filled_set ^ other_set #=>{1, 2, 6}
print("filled_set ^ other_set:",filled_set ^ other_set)

#判断左边的集合是不是右边的超集
{1,2} >= {1,2,3} #=>false

#判断左边是不是右边的子集
{1,2} <= {1,2,3} #=>True

#用in来判断元素在集合中是否存在
2 in filled_set #=>True
10 in filled_set #=>False





