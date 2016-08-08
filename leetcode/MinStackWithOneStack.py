class Stack():
    def __init__(self):
        self.s = []
        self.size = 0

    def push(self, x):
        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

        self.s.append(x)
        self.size += 1

    def pop(self):
        if self.s:
            outItem = self.s.pop()
            self.size -= 1

            if outItem == self.min[-1]:
                self.min.pop()

            return outItem


    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.min[-1]

    def getsize(self):
        print 'the min stack'
        print (self.min)
        print 'the  stack'
        print self.s


s = Stack()
s.push(-2)
s.push(-2)
s.push(0)
s.push(-1)
print '*************************************get size'
s.getsize()
print '*************************************get size'
print s.getMin()
s.top()
s.pop()
print s.getMin()
print '*************************************get size'
s.getsize()
print '*************************************get size'