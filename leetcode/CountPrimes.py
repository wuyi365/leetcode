class Solution(object):
    def isPrime(self, n):
        if n <= 2:
            return True
        
        z = n / 2
        for i in range(2, z+1):
            if n % i == 0:
                return False
        
        return True
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        s = 0
        for i in range(1, n):
            if self.isPrime(i):
                s += 1
        return s
        
     
     
a = Solution()
s = 7

print a.isPrime(s)
print a.countPrimes(s)