class Solution:
    def MinSum(self, nums: list[int]) -> int:
        best_end = nums[0]
        best_ans = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = best_end + nums[i]

            best_end = min(v1 , v2)
            best_ans = min(best_ans,best_end)

        return best_ans   

    def MaxSum(self, nums: list[int]) -> int:
        best_end = nums[0]
        best_ans = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = best_end + nums[i]
            best_end = max(v1 , v2)
            best_ans = max(best_ans,best_end)
        return best_ans  

    def arraySum(self, nums: list[int]) -> int:
        Asum = 0
        for i in range(len(nums)):
            Asum += nums[i]
        return Asum    


    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        A1 = self.MaxSum(nums)
        if A1 < 0:
            return A1
        A2 = self.arraySum(nums) - self.MinSum(nums) 
        return max(A1,A2)
        