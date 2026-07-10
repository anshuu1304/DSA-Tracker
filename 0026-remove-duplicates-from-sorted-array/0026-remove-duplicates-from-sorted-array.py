class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        read_idx = 1
        write_idx =0
        unique_cnt = 1

        while read_idx < len(nums):

            if nums[read_idx] == nums[read_idx-1]:
                read_idx+=1
                continue
            else:
                nums[write_idx+1] = nums[read_idx]
                read_idx+=1
                write_idx+=1
                unique_cnt+=1  
                
        return unique_cnt          
        