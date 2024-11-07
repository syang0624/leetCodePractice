from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # maxHeap = []
        # for row in matrix:
        #     for num in row:
        #         heapq.heappush(maxHeap, -num)
        #         if len(maxHeap) > k:
        #             heapq.heappop(maxHeap)

        # return -maxHeap[0]
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            totalCount = 0
            for row in matrix:
                currentCount = 0
                for value in row:
                    if value <= mid:
                        currentCount += 1
                    else:
                        break
                totalCount += currentCount
            if totalCount < k:
                left = mid + 1
            else:
                right = mid
        return left


# Time: O(n * log(max - min))
# Space: O(1)
