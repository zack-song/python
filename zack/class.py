# 类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，无法在类外部直接访问
    __weight = 0
    #定义构造方法
    #类中的方法和函数的不同是，方法的第一个参数必须是self，self不是关键字，可用其他代替,self是类的实例
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("{0.name}说：我{0.age}岁。".format(self))
    #定义私有方法，无法在类外部调用
    def __speak(self):
        print("这是个私有方法")


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        # people.__init__(self, n, a, w)
        #也可以用super方法
        super(student, self).__init__(n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  #若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。