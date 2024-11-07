class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineSet = {}
        for x in magazine:
            if x in magazineSet:
                magazineSet[x] += 1
            else:
                magazineSet[x] = 1
        for y in ransomNote:
            if y not in magazineSet:
                return False
            elif y in magazineSet and magazineSet[y] > 0:
                magazineSet[y] -= 1
            else:
                return False
        return True
