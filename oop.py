#---- class ----#
import random
class myclass(object):
    var = 10
    def __init__(self):
        print("__init__")
        self.initval = 0
    def test(self, val):
        self.value = val
    def get_test(self):
        return self.value

    def randomnum(self):
        self.num = random.randint(1,10)

this_object = myclass() #call __init__

print(this_object.var)
this_object.test(10)
this_object.get_test()

this_object.randomnum()
print(this_object.num)

#---- inheritance ----#

class Date(object):  #inherited -> parent / base / super class
    def __init__(self,name):
        self.name = name
    def get_date(self):
        return "date"
class Time(Date):  #inheriting -> child / derived / sub class
    def __init__(self,name):
        super(Time,self).__init__(name)
    def get_time(self):
        return "time"

dt = Date("b")
print(dt.get_date())

tm = Time("a")
print(tm.get_date())
print(tm.get_time())
print(tm.name)

#---- multiple inheritance ----#
class A(object):
    def dothis(self):
        print("dothis in A")

class B(A):
    pass

class C(object):
    def dothis(self):
        print("dothis in C")

class D(B,C):
    pass

d_instance = D()
d_instance.dothis()  # depth first search, go to A
print(D.mro()) #D B A C