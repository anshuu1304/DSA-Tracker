import java.util.*;
class Solution {
    public int[] sortedSquares(int[] nums) {

        List<Integer> pos = new ArrayList<>();
        List<Integer> neg = new ArrayList<>();

        for(int num : nums)
        {
            if(num >= 0)
            {
                pos.add(num*num);
            }
            else
            {
                neg.add(num*num);
            }
        }

        Collections.reverse(neg);

        int i = 0;
        int j = 0;
        int idx= 0;
        int n = neg.size();
        int m = pos.size();
        int[] res = new int[nums.length];

        while(i < m && j < n)
        {
            if(pos.get(i) <=  neg.get(j))
            {
                res[idx] = pos.get(i);
                idx++;
                i++;
            }
            else
            {
                res[idx] = neg.get(j);
                idx++;
                j++;
            }
        }
        
        while(i < m)
        {
            res[idx] = pos.get(i);
            idx++;
            i++;
        }
        while(j < n)
        {
            res[idx] = neg.get(j);
            idx++;
            j++;
        }

        return res;
    }
}