class Solution {
    private boolean canSplit(int[] nums, int k , int maxSum)
    {
        int currentSum = 0;
        int partitions = 1;

        for(int num : nums)
        {
            if(currentSum + num <= maxSum)
            {
                currentSum += num;
            }
            else
            {
                partitions++;
                currentSum = num;
            }
        }
        return partitions <= k;
    }
    public int splitArray(int[] nums, int k) {

        int low = 0;
        int high = 0;

        for(int num : nums)
        {
            low = Math.max(low , num);
            high += num;
        }
        
        int ans =0;

        while(low <= high)
        {
            int mid = low+(high - low)/2;

            if(canSplit(nums , k , mid))
            {
                ans = mid;
                high = mid-1;
            }
            else
            {
                low = mid+1;
            }
        }
        return ans;
    }
}