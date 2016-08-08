class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        

        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

        self.s.append(x)
        self.size += 1
        

    def pop(self):
        """
        :rtype: nothing
        """
        tmp = self.s.pop()
        self.size -= 1
        if tmp == self.min[-1]:
            self.min.pop()
        return tmp
            
    def getMin(self):
        return self.min[-1]

    def getsize(self):
        print 'the min stack'
        print self.min
        print 'the  stack'
        print self.s


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.s == []
        
        
s = MinStack()
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