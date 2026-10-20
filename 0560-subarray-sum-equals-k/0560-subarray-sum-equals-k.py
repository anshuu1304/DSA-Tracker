class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum =0
        dict = {0:1}
        count = 0

        for i in range(len(nums)):

            curr_sum += nums[i]

            count += dict.get(curr_sum-k ,0)

            dict[curr_sum] = dict.get(curr_sum,0)+1

        return count    

        