from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                check_left = (i == 0) or (flowerbed[i - 1] == 0)
                check_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if check_left and check_right:
                    count += 1
                    flowerbed[i] = 1
                    if count == n:
                        return True
        
        return count >= n