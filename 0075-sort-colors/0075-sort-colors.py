class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes =0
        ones=0
        twos=0

        for num in nums:
            if num == 0:
                zeroes+=1
            elif num == 1:
                ones+=1
            else:
                twos+=1

        for i in range(len(nums)):
            if zeroes > 0:
                nums[i] = 0
                zeroes-=1
            elif ones > 0:
                nums[i] = 1
                ones-=1
            else:
                nums[i] = 2
                twos-=1                        