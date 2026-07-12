class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        min_sum = 0
        diff = 0

        for i in range(n-2):

            left = i+1
            right = n-1

            while left < right:

                sum = nums[i]+nums[left]+nums[right]

                if sum == target:
                    return sum
                    break
                    # left+=1
                    # right-=1
                elif sum < target:
                    diff = abs(target-sum)
                    left+=1
                else:
                    diff = abs(target-sum)
                    right-=1  

                if diff < min_diff:
                    min_diff=diff
                    min_sum = sum 
        
        return min_sum 


        