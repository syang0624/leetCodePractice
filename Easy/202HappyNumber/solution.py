class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        next_number = str(n)
        def simulation(x):
            num = 0
            for i in x:
                num += int(i) ** 2
            return num
        
        while next_number != 1:
            next_number = simulation(str(next_number))
            if next_number in visited:
                return False
            visited.add(next_number)
        return True


# Time Complexity: O(log N)
# Space Complexity: O(1)