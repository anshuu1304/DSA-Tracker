class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        low = 0
        res =float('inf')
        sum =0

        for high in range(len(nums)):

            sum+=nums[high]

            while sum >= target:

                length = high -low+1
                res = min(res , length)

                sum -= nums[low]
                low+=1  

        return 0 if res == float('inf') else res             