from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        players = sorted(players)
        trainers = sorted(trainers)

        j = 0
        for i in range(len(players)):
            while j < len(trainers):
                if players[i] <= trainers[j]:
                    count += 1
                    j += 1
                    break
                j += 1
        return count

# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)