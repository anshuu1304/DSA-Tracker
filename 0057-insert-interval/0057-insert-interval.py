class Solution:
    def mergeIntervals(self, intervals:list[list[int]]) -> list[list[int]]:

        if not intervals:
            return []

        intervals.sort()

        res = []
        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1,len(intervals)):

            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:

                end1 = max(end1,end2)
                continue

            res.append([start1,end1])

            start1 = start2
            end1 = end2

        res.append([start1,end1])

        return res            
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        res = intervals.copy()
        res.append(newInterval)

        return self.mergeIntervals(res)
        