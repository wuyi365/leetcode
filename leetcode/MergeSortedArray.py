# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# Subscribe to see which companies asked this question



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]





    def merge2(self, nums1, m, nums2, n):
    	nums1.extend(nums2)
    	nums1.sort()
    	return nums1


        






import time
c = time.time()
a = Solution()
#b = [0,0,0,0]
nums1 = [1, 2, 3, 4]
m = len(nums1)

nums2 = [3, 4, 5]
n = len(nums2)
print a.merge(nums1, m, nums2, n)
print a.merge2(nums1, m, nums2, n)
print time.time() -c 