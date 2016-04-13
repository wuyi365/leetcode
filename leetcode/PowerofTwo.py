# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
            
        if abs(n % 2) == 1:
            return False
            
        while n % 2 == 0 and n != 1:
            n = n/2
        print n
        if abs(n) == 1:
            return True
        else:
        	return False
        


a = Solution()

print a.isPowerOfTwo(1021)