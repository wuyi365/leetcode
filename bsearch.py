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



a = [i for i in xrange(30)]
b = xrange(20)
print a
print b

#print bsearch(a, 15)



#
#Search a sorted array for the first element larger than k 

def bsearchK(lst, tgt):
    lft = 0
    rgt = len(lst) - 1
    find = False
    while lft <= rgt and not find:
        mid = (lft + rgt) / 2
        print mid
        print '--lft and rgt---'
        print lst[lft]
        print lst[rgt]
        print '-----'
        print lst[mid]
        if tgt == lst[mid]:
            return mid + 1
        elif tgt < lst[mid]:
            print '****tgt < lst[mid]:'
            if tgt >= lst[mid - 1]:
                return mid
            else:
                rgt = mid -1
        elif tgt > lst[mid]:
            print '^^^^^^tgt > lst[mid]'
            if tgt < lst[mid + 1]:
                return mid + 1
            else:
                lft = mid + 1

    return find

print bsearchK(a, 30)