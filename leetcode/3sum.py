# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},

#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)


#s = [-1, 0 ,1 ,2 ,-1, -4]
#s = [11,4,9,-7,-7,4,-6,13,12,-1,-5,-15,-2,-4,7,14,14,13,-2,-11,-9,-3,-15,6,-4,14,-7,-15,2,2,7,-10,13,-6,-1,14,5,8,12,3,14,-15,3,-10,-4,-12,-11,-4,-14,-6,-8,14,6,-15,5,10,14,13,10,-6,-8,-6,-1,-9,3,13,-10,-6,-1,9,4,-2,9,14,3,-9,-13,-1,-6,10,8,-7,9,-8,-7,-1,9,-15,-3,4,-6,5,13,8,3,-6,-1,8,-5,13,2,14,-12,-11,13,-1,-13,8,13,-4,3,-1,-4,-2,-2,5,12,-8,5,-13,3,14]
s = [0,0,0,0]
rst = []
print s
print s.sort()
print s
n = len(s)
from datetime import datetime
import time
a = time.time()
for i in xrange(n- 2):
    if i >= 1 and s[i] == s[i -1]:
        continue
    x = s[i]
    y = i + 1
    z = n - 1
    while y < z:
        sum3 = x + s[y] + s[z]
        if sum3 == 0:
            #yield (x, s[y], s[z])
            #print 'find one...'
            #if not (x, s[y], s[z]) in rst:
            rst.append((x, s[y], s[z]))

            y += 1
            z -= 1
            while y < z and nums[y] == nums[y-1]: y +=1
            while y < z and nums[z] == nums[z + 1]: z -=1
        elif sum3 > 0:
        	z -= 1
        elif sum3 < 0:
        	y += 1


print rst
print time.time() -a 
