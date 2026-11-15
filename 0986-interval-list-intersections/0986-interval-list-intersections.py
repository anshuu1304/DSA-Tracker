class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:

        res =[]
        i=0
        j=0

        while i<len(firstList) and j<len(secondList):

            start1 ,end1 = firstList[i]
            start2 , end2 = secondList[j]

            if start1 <= start2:

                if end1 >= start2:

                    s = max(start1 , start2)
                    e = min(end1,end2)
                    res.append([s,e])
            else:

                if end2 >= start1:

                    s = max(start1 , start2)
                    e = min(end1,end2)
                    res.append([s,e])

            if end1 <= end2:
                i+=1
            else:
                j+=1

        return res                    

        