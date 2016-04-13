# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].


class Solution(object):
    def generate(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lst = [0] * rowIndex

        for i in xrange(rowIndex):
        	if i == 0:
        		lst[i] = [1]
        	if i == 1:
        		lst[i] = [1, 1]
        	else:
        		lst[i] = [0] * (i + 1)
        		lst[i][0] = lst[i][i] = 1
        		for j in range(1, i):
        			lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1] 

        return lst[rowIndex - 1]
        


a = Solution()

print a.generate(3)  