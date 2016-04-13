# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# For example:

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# Hint:


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10: return num
        a = 0
        while num  > 0:
            a += num % 10
            num =  (num / 10)
            # print a
            # print num
        return self.addDigits(a)


    def addDigits2(self, num):
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
            print num
        return num

        

        

num = 1199
b = Solution()
a=b.addDigits(num)
#print(a)# your code goes here
print b.addDigits2(num)