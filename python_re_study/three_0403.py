
###############
#3.control
###############




#定义变量
some_var=5


#这是if语句，注意缩进，在python里缩进非常重要
#结果是打印“some_var is amaller then 10”
if some_var > 10:
    print ("some_var is totally bigger than 10.")
elif some_var < 10:
    print ("some_var is smaller then 10.")
else:
    print ("some_var is indeed 10.")


"""
用for 去便利list
打印结果：
 dog is a mammal
 cat is a mammal
 mouse is a mammal

"""

for animal in ["dog","cat","mouse"]:
    print("{0} is a mammal ".format(animal))

"""
"range(number)"返回1个列表，列表里包含一组数字
从0到number,不包含number
打印：
    0
    2
    3
    4
"""

for i in range(4):
    print (i)



"""
"range(lower,upper)"返回1个列表，列表里包含一组数字
范围从lower 到upper
打印：
    4
    5
    6
    7
"""

for i in range(4,8):
    print(i)



"""
while会一直循环到条件不再满足为止
打印：
    0
    1
    2
    3
"""
x=0
while x<4:
    print (x)
    x+=1

#try/except 代码库（block）用来处理异常
#适用于2.6及以上版本：
try:
    #使用“raise”来抛出异常
    raise IndexError ("This is an index error")
except IndexError as e:
    pass #pass就是啥也不做，一般情况下，你会在这里做异常的处理
except (TypeError,NameError):
    pass #如果需要的话可以一次性处理多个异常
else:    #else分支是可选的，必须出现在所有的except分支之后
    print("All good!")
finally: #最后一定会执行
    print("We can clean up resources here")

#除了使用try/finally之外，我们可以用with语句来进行适当的简化
with open ("myfile.txt") as f:
    for line in f :
        print (line)
        

