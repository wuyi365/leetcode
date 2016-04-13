import random

print random.randint(1, 100)

aa = [random.randint(1, 100) for i in xrange(10)]


my_randoms = random.sample(xrange(100), 10)

def qsort(testList):
	ll = len(testList)

	if ll < 2:
		return testList

	curs = testList[0]
	lft = []
	rgt = []

	for i in testList[1:]:
		if i <= curs:
			lft.append(i)
		else:
			rgt.append(i)
	print '---lft and rgt----'
	print lft
	print rgt
	return qsort(lft) + [curs] + qsort(rgt)


print qsort(aa)