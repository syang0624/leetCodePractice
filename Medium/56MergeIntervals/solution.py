from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        merged_lst = []
        for interval in intervals:
            if not merged_lst or merged_lst[-1][1] < interval[0]:
                merged_lst.append(interval)
            else:
                merged_lst[-1] = [merged_lst[-1][0],
                                  max(merged_lst[-1][1], interval[1])]
        return merged_lst
