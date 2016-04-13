# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lst = []
        nums = nums + [nums[-1]]
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        j = 0
        start = nums[0]
        for i in xrange(0, n - 1):

            if nums[i] == nums[i + 1] - 1:
                j += 1
                continue
            
            else:
                if j == 0:
                    lst.append(str(start))
                else:
                    end = nums[i]
                    lst.append(str(start) + '->' +str(end))
                    j = 0
            start = nums[i + 1]

        return lst


        


a = Solution()

#nums = [0,1,2,4,5,7, 8, 10, 12, 13, 14,17]
nums = [0,1]
print a.summaryRanges(nums)  