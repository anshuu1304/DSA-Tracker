class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n= len(nums)
        low =0
        high = k-1
        window_sum = 0
        window_avg = 0

        for i in range(low , high+1):

            window_sum +=nums[i]
            
        res = window_sum /k

        while high < n-1:

            low+=1
            high+=1

            window_sum -= nums[low-1]
            window_sum += nums[high]

            window_avg = window_sum/k
            res = max(res , window_avg)    

        return res
        