class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        best_ending = nums[0]
        best_ans = nums[0]

        for i in range(1,len(nums)):

            v1 = nums[i]
            v2 = best_ending + nums[i]

            best_ending = max(v1 , v2)
            best_ans = max(best_ans , best_ending)

        return best_ans    
        