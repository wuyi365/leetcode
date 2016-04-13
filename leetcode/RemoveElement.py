# Given an array and a value, remove all instances of that value in place and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example:
# Given input array nums = [3,2,2,3], val = 3

# Your function should return length = 2, with the first two elements of nums being 2.




class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print 'begin.....'
        print nums
        print val
        if not nums: return 0
        A = 0

        for n in nums:
            if n != val: 
                nums[A] = n
                print '------------aa--'
                print n
                print nums



                A += 1
        return A
        
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:
        	if i == val:
        		nums.remove(i)
        return len(nums)


a = Solution()

nums = [3,2, 1,2,3]
val = 3

print a.removeElement(nums, val)