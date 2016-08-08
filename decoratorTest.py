
from time import time

def timelog(func, cur_evaluating = set()):
	def timcost(*args, **kw):
		if func not in cur_evaluating:
			startTime = time()
			print 'calling function...' + func.__name__
			r = func(*args, **kw)
			endTime = time()
			gap = endTime - startTime
			print 'Time cost ' + str(gap)
		else:
			r = func(*args, **kw)
		return r

	return timcost


@timelog
def testFunc():
	for i in range(10000000):
		if  i % 50000 == 0:
			print 'good for 20000'
		pass


testFunc()


