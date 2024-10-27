from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1

        if len(set(count)) == len(set(count.values())):
            return True
        else:
            return False
