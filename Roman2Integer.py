class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Maps = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sums = 0
        n = len(s)
        for i in xrange( n - 1):
        	# this is something like IV, sum should + V - I
        	#
        	if Maps[s[i]] < Maps[s[i + 1]]:
        		sums -= Maps[s[i]]
        	else:
        		sums += Maps[s[i]]

        sums += Maps[s[n - 1]]

        return sums




a = Solution()
s = 'DIV'
print a.romanToInt(s)
