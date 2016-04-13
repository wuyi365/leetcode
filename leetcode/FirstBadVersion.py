# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lft = 0
        rgt = n - 1
        found = False
        while lft <= rgt and not found:
            mid = (lft + rgt) / 2
            if isBadVersion(mid):
            	end =  mid
            else:
            	start = end
