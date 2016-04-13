class Solution:
    # @param nums, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, nums, target):
        left=0
        right=len(nums)-1
        if target<nums[left] or target>nums[right]: return [-1,-1]
        while left<=right:
            mid=int((left+right)/2)
            if nums[mid]==target:
                left=mid
                while left>=0 and nums[left]==target:
                    left=left-1
                right=mid
                while right<len(nums) and nums[right]==target:
                    right=right+1
                return [left+1,right-1]
            if target<nums[mid]:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return [-1,-1]
 
nums=[1,2,2,2, 2,3]
b = Solution()
a=b.searchRange(nums,2)
print(a)# your code goes here