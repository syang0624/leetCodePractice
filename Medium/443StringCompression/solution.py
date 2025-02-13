from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        result = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[result] = chars[i]
            result += 1
            if group_length > 1:
                string = str(group_length)
                chars[result:result + len(string)] = list(string)
                result += len(string)
            i += group_length
        return result
    
# Time Complexity: O(N)
# Space Complexity: O(1)