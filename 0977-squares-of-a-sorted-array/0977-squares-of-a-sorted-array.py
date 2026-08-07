class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        pos =[]
        neg =[]

        for num in nums:
            if num >=0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(len(pos)):
            pos[i] = pos[i]*pos[i]
        for j in range(len(neg)):
            neg[j] = neg[j]*neg[j]

        neg.reverse()

        i=0
        j=0
        res = [] 
        m = len(pos)
        n = len(neg)

        while i<m and j<n:

            if pos[i] <= neg[j]:
                res.append(pos[i])
                i+=1
            else:
                res.append(neg[j])
                j+=1

        while i<m:
            res.append(pos[i])
            i+=1

        while j<n:
            res.append(neg[j])
            j+=1
                    
        return res            

                   
        