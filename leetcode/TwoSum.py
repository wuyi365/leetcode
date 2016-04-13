# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in xrange(n):
            for j in xrange(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i, j]



nums = [3,2,4]
target = 6
print twoSum(nums, target)