# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

# Note that 1 is typically treated as an ugly number.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

import math
def isUgly(num):
    if num == 1: return True
    lst = [2,3,5,6, 10, 15, 30]
    for i in lst:
        a = math.log(abs(num),i)
        if a == int(a):
            return True
    return False




print isUgly(-2147483648)