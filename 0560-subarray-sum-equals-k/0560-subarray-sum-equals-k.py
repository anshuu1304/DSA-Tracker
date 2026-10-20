class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        currSum = 0
        count = 0
        dict = {0:1}

        for i in range(len(nums)):

            currSum += nums[i]

            count += dict.get(currSum-k,0)

            dict[currSum] = dict.get(currSum , 0)+1

        return count   

        