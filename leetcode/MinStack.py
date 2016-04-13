class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s:
            return self.s.pop()
            
    def getMin(self):
        news = []
        while self.s:
            news.append(self.s.pop())
        
        news.sort()
        if news:
            return news[0]
        else:
            return None



    def top(self):
        """
        :rtype: int
        """
        if self.s:
            return self.s[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.s == []
        
        
s = MinStack()
s.push(-3)
print s.getMin()