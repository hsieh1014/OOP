class MaxSizeList(object):
    def __init__(self,max):
        self.max_size = max
        self.innerlist = []

    def push(self, obj):
        if len(self.innerlist) < self.max_size:
            self.innerlist.append(obj)
        else:
            self.innerlist.pop(0)
            self.innerlist.append(obj)

    def get_list(self):
        return self.innerlist

a = MaxSizeList(3)
a.push("a")
a.push("b")
a.push("c")
a.push("d")
a.push("e")
print(a.get_list())