from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged = nums1 + nums2
        # merged = sorted(merged)
        # k = len(merged)
        # if k % 2 == 1:
        #     return merged[k // 2]
        # else:
        #     return (merged[k // 2] + merged[k // 2 - 1]) / 2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = nums1[i] if i >= 0 else float("-inf")
            Aright = nums1[i + 1] if (i + 1) < len(nums1) else float("inf")
            Bleft = nums2[j] if j >= 0 else float("-inf")
            Bright = nums2[j + 1] if (j + 1) < len(nums2) else float("inf")

            # partition is correct:
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# Time Complexity: O(log (m+n))
# Space Complexity: O(1)