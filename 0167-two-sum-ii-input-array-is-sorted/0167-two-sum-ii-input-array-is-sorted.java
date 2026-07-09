class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int i = 0; 
        int j = numbers.length-1;

        while(i < j)
        {
            int curr_sum = numbers[i]+numbers[j];

            if(curr_sum == target)
            {
                return new int[]{i+1,j+1};
            }

            if(curr_sum < target)
            {
                i++;
            }
            else if(curr_sum > target)
            {
                j--;
            }
        }
        return new int[]{};
    }
}