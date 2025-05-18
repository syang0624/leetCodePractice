class Solution:
    def intToRoman(self, num: int) -> str:
        value_map = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

        roman_numeral = ""
        for symbol, value in value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Time Complexity: O(1)
# Space Complexity: O(1)