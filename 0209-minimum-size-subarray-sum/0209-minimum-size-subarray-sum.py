class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
         n = len(nums)
         low = 0
         high = 0
         curr_sum = 0
         res = float('inf')


         while high < n:

            curr_sum += nums[high]

            while curr_sum >= target:

                min_len = high - low+1
                res = min(res , min_len)

                curr_sum -= nums[low]
                low+=1

            high+=1

         return 0 if res == float('inf') else res       



        