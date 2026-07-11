class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0 
        res =[0]*(m+n)
        idx =0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[idx] = nums1[i]
                i+=1
                idx+=1
            else:
                res[idx] = nums2[j]
                j+=1
                idx+=1

        while i < m:
            res[idx] = nums1[i]
            i+=1
            idx+=1

        while j < n:
            res[idx] = nums2[j]
            j+=1
            idx+=1

        for k in range(m+n):
            nums1[k] = res[k]  



        