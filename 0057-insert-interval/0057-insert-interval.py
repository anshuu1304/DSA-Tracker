class Solution:
    def mergeInterval(self,res : list[list[int]]):
        if not res:
            return []

        res.sort()

        ans = []

        start1 = res[0][0]
        end1 = res[0][1]

        for i in range(1,len(res)):

            start2 = res[i][0]
            end2 = res[i][1]

            if end1 >= start2:

                end1 = max(end1, end2)
                continue

            ans.append([start1,end1])

            start1 = start2
            end1 = end2

        ans.append([start1,end1])
        return ans

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = intervals.copy()

        res.append(newInterval)

        return self.mergeInterval(res)