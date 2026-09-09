class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        diff = 0
        min_diff = float('inf')
        min_sum = 0

        for i in range(n-2):

            left = i+1
            right = n-1

            while left < right:

                curr_sum = nums[i]+nums[left]+nums[right]

                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    diff = abs(target-curr_sum)
                    left+=1
                else:
                    diff = abs(target-curr_sum)
                    right-=1

                if diff < min_diff:
                    min_diff = diff
                    min_sum = curr_sum
        
        return min_sum


        