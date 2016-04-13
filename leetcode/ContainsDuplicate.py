# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

# Subscribe to see which companies asked this question

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        dict = {}
        for i in xrange(n):
            if not nums[i] in dict:
                dict[nums[i]] = i
            else:
                prev = dict[nums[i]]
                if i - prev <= k:
                    print dict
                    return True
                else:
                    dict[nums[i]] = i

            
                
        return False




a = Solution()
#b = [0,0,0,0]
b = [-1,0, 1 ,2, -1, -4]
print a.containsNearbyDuplicate(b, 5)
print time.time() -c 