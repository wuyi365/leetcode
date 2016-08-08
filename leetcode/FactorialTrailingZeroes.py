# Given an integer n, return the number of trailing zeroes in n!.

# # Note: Your solution should be in logarithmic time complexity.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # how many 5, how many 10
        #60
        total = 0
        i = 1
        while 5**i <= n:
            total += int(n/(5**i))
            i += 1

        print i
        return total

a = Solution()
print a.trailingZeroes(5)