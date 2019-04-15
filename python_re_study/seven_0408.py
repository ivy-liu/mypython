#####################################
#7.高级内容
#####################################

#生成器
#生成器会动态生成一些数据，而不是在使用数据前创建数据，然后把这些数据存储起来

#下面的方法（非生成器）会将所有的值翻倍，并存在double_arr变量里
#如果iterable很大得话，double_arr将是巨大的
def double_number(iterable):
    double_arr =[]
    for i in iterable:
        double_arr.append(i+i)
    return double_arr


#运行下面的代码意味着我们首先会将所有的值都加倍，然后返回回来
#最后在检查返回值是否符合特定条件
for value in double_number(range(1000000)):
    print (value)
    if value>5:
        break


#我们可以使用生成器来动态加倍必要的值
def double_number_generator(iterable):
    for i in iterable:
        yield i+i

#使用生成器运行之前同样的代码
#现在我们根据运行时逻辑一个接一个的进行加倍
#一旦value>5，代码就会break
#这样我们就不需要把所有的值都加倍1遍了（运行速度会快很多）
#因为 python3 中取消了 range 函数，而把 xrange 函数重命名为 range，所以现在直接用 range 函数即可。
for value in double_number_generator(range(1000000)):
    print (value)
    if value >5:
        break

#BTW：你注意到 'range' 用在了 'test_non_generator' 而 'xrange' 用在 'test_generator' 里了吗？
#就像 'double_number_generator' 是 'double_number' 的生成器版本一样
#'xrange' 是 'range' 的生成器版本
#'range' 会返回包含1000000个值的列表
#'xrange' 回在我们遍历的时候动态依次创建1000000个值

#你也可以像使用列表表达式一样使用生成器表达式
values=(-x for x in [1,2,3,4,5])
for x in values:
    print(x) 

#你也可以直接把生成器转换成列表
values=(-x for x in [1,2,3,4,5])
gen_to_list=list(values)
print(gen_to_list) #=>[-1, -2, -3, -4, -5]

#装饰器
#装饰器是高阶函数，可以接受函数作为参数并返回函数
#简单的例子 add_apples 装饰器会将'Apple'元素插入 into
#到目标函数（被装饰的函数）get_fruits返回的列表里
def add_apples(func):
        def get_fruits():
                fruits=func()
                fruits.append('Apple')
                return fruits
        return get_fruits
@add_apples
def get_fruits():
        return ['Banana','Mango','Orange']

#打印出的结果里是包含'Apple'元素的
#Banana,Mango,Orange,Apple
print(','.join(get_fruits()))

#下面的例子里beg 装饰了say
#Beg 会调用say.如果say_please 是True 那么bey 回修改say的返回值
#message

