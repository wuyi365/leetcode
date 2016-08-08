import time

def timeCost(func):
	def wrap(*arg, **kw):
		startTime = time.time()
		func(*arg, **kw)
		gap = time.time() - startTime
		print 'calling method....' + func.__name__ + ' cost time: '
		print  gap

	return wrap

#@timeCost
def fibBasic(n):
	if n < 2:
		return n
	else:
		return fibBasic(n -1) + fibBasic(n -2) 




def fib(n):
	a,b = 0,1
	for i in range(n):
		print 'adding i'
		a,b = b,a+b
        yield a
	#print a


def fib2(n):
    a,b = 0,1
    #restf = []
    for i in xrange(n):
        #print 'adding i'
        a,b = b,a+b
        yield a
        #print b
        #restf.append(a)
    return a

n = 50
for i in fib2(n):
    print i