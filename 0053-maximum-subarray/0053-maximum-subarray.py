class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        best_end = nums[0]
        best_ans = nums[0]

        for i in range(1,len(nums)):

            v1 = nums[i]
            v2 = best_end + nums[i]

            best_end = max(v1,v2)

            best_ans = max(best_ans,best_end)

        return best_ans    
        