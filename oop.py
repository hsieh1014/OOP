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

class Date(object):  #inherited -> parent / base / super class
    def get_date(self):
        return "date"
class Time(Date):  #inheriting -> child / derived / sub class
    def get_time(self):
        return "time"

this_object = myclass() #call __init__

print(this_object.var)
this_object.test(10)
this_object.get_test()

this_object.randomnum()
print(this_object.num)

dt = Date()
print(dt.get_date())

tm = Time()
print(tm.get_date())
print(tm.get_time())