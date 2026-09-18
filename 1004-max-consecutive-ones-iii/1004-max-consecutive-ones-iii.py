class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        low = 0
        res = 0
        zeroes = 0

        for high in range(len(nums)):

            if nums[high] == 0:
                zeroes+=1

            while zeroes > k:

                if nums[low] == 0:
                    zeroes-=1

                low+=1

            length = high - low+1
            res = max(res , length)   

        return res             

        