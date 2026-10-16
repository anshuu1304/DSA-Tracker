class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        left = 0
        total = sum(nums)

        for i in range(len(nums)):

            right = total - nums[i] - left

            if left == right:
                return i

            left += nums[i]    

        return -1    
        