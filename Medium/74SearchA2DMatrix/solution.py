from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if target == arr[mid]:
                    return True
                elif target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                if binarySearch(matrix[i], target):
                    return True
                else:
                    return False
        return False
