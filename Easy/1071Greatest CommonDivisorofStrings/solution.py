class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        len1, len2 = len(str1), len(str2)

        def isDivisor(length):
            if len1 % length or len2 % length:
                return False
            f1, f2 = len1 // length, len2 // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for length in range(min(len1, len2), 0, -1):
            if isDivisor(length):
                return str1[:length]


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#             len1, len2 = len(str1), len(str2)

#             def isDivisor(l):
#                 if len1 % l or len2 % l:
#                     return False
#                 f1, f2 = len1 // l, len2 // l
#                 return str1[:l] * f1 == str1 and str1[:l] * f2 == str2


            
#             for l in range(min(len1, len2), 0, -1):
#                 if isDivisor(l):
#                     return str1[:l]
            
#             return ""