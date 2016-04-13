class Queues:
	def __init__(self, queue = []):
		self.q = queue

	def qput(self, i):
		#self.q.insert(0,i)
		self.q.append(i)

	def qempty(self):
		return len(self.q) == 0

	def qpop(self):
		return self.q.pop(0)

	def qsize(self):
		return len(self.q)

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = Queues()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s.qput(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s.qsize() == 1:
        	print 'aaaaaaaaaaa'
        	return self.s.qpop()
        else:
        	print 'bbbbbbbbbbbbbb'
        	n = self.s.qsize()
        	print n
        	newS = Queues()
        	while n > 1:
        		i = self.s.qpop()
        		print i
        		newS.qput(i)
        		n -= 1
        	last = self.s.qpop()
        	print '----------------------zzz'

        	self.s = newS
        	return last



    def top(self):
        """
        :rtype: int
        """
        if self.s.qsize() == 1:
        	i = self.s.qpop()
        	self.s.push(i)
        	return i
        else:
        	n = self.s.qsize()
        	newS = Queues()
        	while n > 1:
        		i = self.s.qpop()
        		newS.qput(i)
        		n -= 1
        	last = self.s.qpop()
        	self.s = newS
        	self.s.qput(last)
        	return last
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.s == []

# s = Queues()

# s.qput('x')
# s.qput('y')
# s.qput('z')
# #print s.top()
# print s.qpop()

s = Stack()

s.push('x')
s.push('y')
s.push('z')
s.push('a')
s.push('b')
print s.top()
print '*****'
print s.pop()