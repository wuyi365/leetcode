class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while 3 * i < n and n <= 3 *(i + 1):
            i += 1
        print i
        gap = n - 3 * i
        print gap
        if gap < 0:
            gap = 0
        
        return (3 ** i) * (2**gap)



a = Solution()

print a.integerBreak(4)