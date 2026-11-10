class Solution:
    def mergeSort(self, nums:list[int], left:int , right:int , lower:int, upper:int):

        if left >= right:
            return 0

        mid = (left+right)//2

        leftCount = self.mergeSort(nums,left, mid, lower,upper)
        rightCount = self.mergeSort(nums,mid+1,right,lower,upper)

        totalCount = leftCount+rightCount

        leftHalf = nums[left:mid+1]
        rightHalf = nums[mid+1:right+1]   

        i =0
        j =0

        for x in leftHalf:

            while i < len(rightHalf) and rightHalf[i] - x < lower:
                i+=1
            while j < len(rightHalf) and rightHalf[j] - x <= upper:
                j+=1

            totalCount += j-i

        nums[left:right+1] = sorted(nums[left:right+1])

        return totalCount    

    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:

        preSum = [0]

        for num in nums:
            preSum.append(preSum[-1]+num)

        return self.mergeSort(preSum,0,len(preSum)-1,lower , upper)    

        