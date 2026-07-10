class Solution {
    public int removeDuplicates(int[] nums) {

        int read_idx = 1;
        int write_idx = 0;
        int unique_cnt = 1;
        int nums_len = nums.length;

        while(read_idx <  nums_len)
        {
            if(nums[read_idx] == nums[read_idx-1])
            {
                read_idx++;
                continue;
            }
            else
            {
                nums[write_idx+1] = nums[read_idx];
                write_idx++;
                read_idx++;
                unique_cnt++;
            }
        }
        return unique_cnt; 
    }
}