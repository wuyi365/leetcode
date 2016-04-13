# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:

class Solution(object):
    def moveZeroes2(self, nums):

        pos = 0
        for i in xrange(len(nums)):
            print 'i: ' + str(i)
            print 'pos: ' + str(pos)
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

            print nums

        return nums
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        
        for i in xrange(pos, len(nums)):
            nums[i] = 0 

        return nums




nums=[1,1,0,3,0, 12]
print '--------------------orig is'
print nums
b = Solution()
a=b.moveZeroes2(nums)
print '----------------------reustl is'
print(a)# your code goes here