# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return MAX_INT
        goOn = True
        count = 0
        sum = 0

        while sum < dividend:
        	sum += divisor
        	print sum
        	count += 1
        	print count

        return count - 1

 



a = Solution()
print a.divide(0, 1)

