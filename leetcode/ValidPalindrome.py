class Solution(object):
    def validStr(self, i):
        if i.isdigit():
            return True
        if (i.lower() >= 'a' and i.lower() <= 'z'):
            return True
        return False
        
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n <= 1:
            return True
        
        i = 0
        j = n - 1
        while i <= j and j >= 0 and i >= 0:
            while i < j and not self.validStr(s[i]) :
                i += 1
            while i < j and not self.validStr(s[j]):
                j -= 1
            """"print i,j
            print s[i]
            print s[j]
            print s[i].lower() != s[j].lower()"""
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True
            
        
        
        
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        
        stupid but works:
        create a new list with all valid string
        reverse it
        compare with the reverse one
        if equal: true
        else false
        """
        if len(s) <= 1:
            return True
        news = []
        for i in s:
            if i.isdigit():
                news.append(i)
            else:
                if (i.lower() >= 'a' and i.lower() <= 'z'):
                    news.append(i.lower())
        rev = news[::-1]
       
        return news == rev
                
        
        
        
a = Solution()
s = 'A man, a plan, a canal: Panama'
ss = '.,'

print a.isPalindrome(ss)
print a.isPalindrome2(ss)