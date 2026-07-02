class Solution:
    def canSplit(self , nums: List[int] , k : int , maxSum : int) -> bool:

        currentSum = 0
        partitions = 1
        for num in nums:
            if currentSum + num <= maxSum:
                currentSum += num
            else:
                partitions+=1
                currentSum = num
        return partitions <= k                    
    def splitArray(self, nums: List[int], k: int) -> int:

        low = max(nums)
        high = 0
        for num in nums:
            high += num

        ans = 0    

        while low <= high:
            mid = low+(high - low)//2

            if self.canSplit(nums , k , mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans               
        