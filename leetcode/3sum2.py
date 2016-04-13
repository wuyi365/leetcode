class Solution:
    # @return nums[i]list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)                  # For the first item
        for i in xrange(n - 2):
            #remove duplicate sum[i]
            #
            if i >= 1 and nums[i] == nums[i -1]:
                continue
            j = i + 1               # For the middle item
            k = len(nums) - 1        # For the last item
            while j < k:
                # if nums[i]+ nums[j] + nums[j] > 0 or nums[i]+ nums[k]+ nums[k]< 0:
                #     # nums[k] >= any nums[j], nums[j] <= any nums[k]
                #     # Impossible to find a answer in the future
                #     break
                if nums[i]+ nums[j]+nums[k]== 0:
                    # Because the nums is sorted, so the nums[i] <= nums[j] <= nums[k]
                    # And in every round, i or j/k is different from the previous
                    # round. Therefore, the answer [nums[i], nums[j], nums[k]] is new
                    # and unique for the result set.
                    result.append([nums[i], nums[j], nums[k]])
                    # Skip duplicate nums[j-1] and nums[k+1]
                    j += 1
                    while j < k+1 and nums[j] == nums[j-1]:   j += 1
                    k -= 1
                    while k > j-1 and nums[k] == nums[k+1]:   k -= 1
                elif nums[i] + nums[j]+ nums[k]< 0:
                    # Skip duplicate nums[j-1]
                    j += 1
                    while j < k+1 and nums[j] == nums[j-1]:   j += 1
                else:
                    # Skip duplicate nums[k+1]
                    k -= 1
                    while k > j-1 and nums[k] == nums[k+1]:   k -= 1

            # Skip duplicate nums[i-1]
            i += 1
            while i < len(nums)-1 and nums[i] == nums[i-1]:  i += 1

        return result

import time
c = time.time()
a = Solution()
#b = [0,0,0,0]
b = [-1,0, 1 ,2, -1, -4]
print a.threeSum(b)
print time.time() -c 