class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        min_end = nums[0]
        max_end = nums[0]
        best_ans = nums[0]

        for i in range(1 , len(nums)):

            v1 = nums[i]
            v2 = min_end * nums[i]
            v3 = max_end * nums[i]

            min_end = min(v1 , min(v2,v3))
            max_end = max(v1 , max(v2,v3))

            best_ans = max(best_ans , max(min_end , max_end))

        return best_ans    
        