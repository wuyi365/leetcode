def moveZeros(lst):
	n = len(lst)
	j = 0
	for i in xrange(n):
		if lst[i] != 0:
			lst[j] = lst[i]
			j += 1
	print j
	for i in xrange(j,n):
	    lst[i] = 0
    #lst[j:] = 0

	return lst


lst = [0, 0, 1, 3, 0, 2]

print moveZeros(lst)
