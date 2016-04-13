import random


aa = [random.randint(1,10) for i in xrange(5)]

aa = [9, 8, 7, 2, 10]
print aa
def insertion_sort(lst):
    if len(lst) == 1:
        return

    for i in xrange(1, len(lst)):
        temp = lst[i]
        print 'i----->  ' + str(i)
        print temp
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            print 'j... ' + str(j)
            print 'i... ' + str(i)
            print 'after while loop: ', lst
            j -= 1
            
        lst[j + 1] = temp
        print 'after for loop: ', lst
    return lst


print insertion_sort(aa)