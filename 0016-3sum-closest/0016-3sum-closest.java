class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int diff = 0;
        int min_diff = Integer.MAX_VALUE;
        int min_sum = 0;

        for(int i =0; i<n-2; i++)
        {
            int left = i+1;
            int right = n-1;

            while(left < right)
            {
                int curr_sum = nums[i]+nums[left]+nums[right];

                if(curr_sum == target)
                {
                    return curr_sum;
                }
                else if(curr_sum < target)
                {
                    diff = Math.abs(target-curr_sum);
                    left++;
                }
                else
                {
                    diff = Math.abs(target-curr_sum);
                    right--;
                }

                if(diff < min_diff)
                {
                    min_diff = diff;
                    min_sum = curr_sum;
                }
            }
        }
        return min_sum;
    }
}