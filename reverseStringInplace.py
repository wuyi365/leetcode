ll = ['J', 'a', 'b', 'b', 'a', ' ', 'L', 'a', 'c']

n = len(ll)
print n
print n / 2
for i in range(0, n / 2):
	print '---------------i'
	print i
	ll[i], ll[n - i - 1] = ll[n - i -1], ll[i]


print ll