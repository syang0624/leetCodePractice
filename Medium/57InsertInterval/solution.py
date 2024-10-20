from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        lst = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                lst.append(newInterval)
                return lst + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                lst.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]
        lst.append(newInterval)
        return lst
