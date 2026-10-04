class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        
        no_del = arr[0]
        one_del = float('-inf')
        res = arr[0]

        for i in range(1 , len(arr)):

            prev_no_del = no_del
            prev_one_del = one_del

            no_del = max(arr[i] , prev_no_del+arr[i])

            one_del = max(prev_one_del+arr[i] , prev_no_del)

            res = max(res , max(no_del , one_del))

        return res    