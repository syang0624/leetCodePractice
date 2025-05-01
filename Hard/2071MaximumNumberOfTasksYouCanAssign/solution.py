import bisect
from typing import List

class Solution:
    def canAssign(self, mid, workers, tasks, pills, strength):
        usable_workers = sorted(workers[-mid:])
        for i in range(mid - 1, -1, -1):
            task = tasks[i]
            if usable_workers[-1] >= task:
                usable_workers.pop()
            else:
                if pills <= 0:
                    return False
                # Find the weakest worker who can do the task with pill
                idx = bisect.bisect_left(usable_workers, task - strength)
                if idx == len(usable_workers):
                    return False
                pills -= 1
                usable_workers.pop(idx)
        return True
        
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        low, high = 0, min(len(tasks), len(workers))
        assigned = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.canAssign(mid, workers, tasks, pills, strength):
                assigned = mid
                low = mid + 1
            else:
                high = mid - 1
        return assigned
    
# Time Complexity: O(k log² k), where k = min(len(tasks), len(workers))

# Space Complexity: O(k)