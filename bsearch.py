import random


def bsearch(lst, target):
	lft = 0
	rgt = len(lst) - 1
	found = False

	while lft <= rgt and not found:
		mid = (lft + rgt) / 2
		if target == lst[mid]:
			found = True
		else:
			if target < lst[mid]:
				rgt = mid - 1
			elif target > lst[mid]:
				lft = mid + 1
	return found



a = [i for i in xrange0)]
b = xrange(20)
print a

print bsearch(a, 30)