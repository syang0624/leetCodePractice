from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.counter2[old_val] -= 1
        if self.counter2[old_val] == 0:
            del self.counter2[old_val]
        self.nums2[index] = new_val
        self.counter2[new_val] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += self.counter2.get(tot - num, 0)
        return ans



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)