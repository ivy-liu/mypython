##############################
# 5.类
##############################

#以继承objec的方式来定义1个类
class Human(object):
    #类属性，所有类实例都共享

    species="H.sapiens"

    #基本的构造函数，当类实例化的时候会自动被调用
    #注意双下划线开头和结尾的变量是python保留的
    #你不应该自己定义类似风格的变量
    def __init__(self,name):
        #将参数里name赋值个同名的实例属性
        self.name=name

        #初始化属性
        self.age=0
    def say(self,msg):
        return "{0}:{1}".format(self.name,msg)

    #类方法，所有实例共享
    #调用的时候第1个参数代表这个类本身
    @classmethod
    def get_species(cls):
        return cls.species

    #静态方法被调用的时候是不需要传入类或实例的引用（kls,self）的
    @staticmethod
    def grunt():
        return "*grunt*"

    #属性有点像getter.
    #这个将age()方法变成了同名的制度的属性（调用的时候不用加括号了）
    @property
    def age(self):
        return self._age

    #这样就可以允许属性被赋值了
    @age.setter
    def age(self,age):
        self._age=age

    #这样就可以允许属性被删除
    @age.deleter
    def age(self):
        del self._age
        
#实例化1个类
i=Human(name="Ian")
print (i.say("hi"))  #=>Ian:hi

j=Human("Joel")
print(j.say("hello"))  #=>Joel:hello

#调用类方法
i.get_species() 

#修改类属性
Human.species="H.neanderthalensis"
i.get_species()
j.get_species()

#调用静态方法
Human.grunt()

#更新属性
i.age = 42

#获取属性
i.age #=>42

#删除属性
del i.age
i.age #=>抛出AttributeError异常

