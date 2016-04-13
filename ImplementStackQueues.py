class Queues:
	"""
	FIFO
	"""
	def __init__(self, queue = []):
		self.q = queue

	def put(self, i):
		#self.q.insert(0,i)
		self.q.append(i)

	def empty(self):
		return len(self.q) == 0

	def pop(self):
		return self.q.pop(0)

	def size(self):
		return len(self.q)
class Stacks:
	def __init__(self, stack = []):
		self.s = stack

	def put(self, i):
		self.s.append(i)

	def empty(self):
		return len(self.s) == 0

	def pop(self):
		return self.s.pop(-1)

	def size(self):
		return len(self.s)

# a = Queues()

# a.put('z')
# a.put('y')
# print a.pop()
# print a.size()

s = Stacks()

s.put(1)
s.put('x')
s.put('y')
s.put('z')
print s.pop()
print s.size()