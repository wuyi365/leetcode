class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        slist = list(s)
        slistVowels = []
        sposition = []
        for i in xrange(len(slist)):
            if slist[i] in vowels:
                sposition.append(i)
                slistVowels.append(slist[i])
        n = len(sposition)
        for i in xrange(n):
            del slist[sposition[i]]
            slist.insert(sposition[i], slistVowels[n - i - 1])
        
        return ''.join(slist)

    def reverseVowels2(self, s):
        vowels = ['a','e','i','o','u']
        slist = list(s)
        n = len(slist)
        i = 0
        j = n - 1
        while i < j:
            if slist[i].lower() in vowels and slist[j].lower() in vowels:
                tmp = slist[i] 
                slist[i] = slist[j]
                slist[j] = tmp
                i += 1
                j -= 1
                
            elif slist[i].lower() in vowels and not slist[j].lower() in vowels:
                j -= 1
            elif not slist[i].lower() in vowels and slist[j].lower() in vowels:
                i += 1
            elif not slist[i].lower() in vowels and not slist[j].lower() in vowels:
                i += 1
                j -= 1


        return ''.join(slist)

        
s = Solution()
print s.reverseVowels2('aA')