import random


aa = [random.randint(1,100) for i in xrange(10)]

print aa

def bbsort(tstList):
	llen = len(tstList)
	for i in xrange(llen):
		for j in xrange(llen - i - 1):
			if tstList[j] > tstList[j + 1]:
				tstList[j], tstList[j + 1] = tstList[j + 1], tstList[j]

	return tstList

print bbsort(aa)
