class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        int n = nums.length;
        int low = 0;
        int high = 0;
        int subarray_sum = 0;
        int res = Integer.MAX_VALUE;

        while(high < n)
        {
            subarray_sum+=nums[high];

            while(subarray_sum >= target)
            {
                int len  = high-low+1;
                res = Math.min(res, len);

                subarray_sum -= nums[low];
                low++;
            }
            high++;
        }
        
        return (res == Integer.MAX_VALUE) ? 0:res;
    }
}