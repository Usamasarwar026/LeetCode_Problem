class Solution:
    def romanToInt(self, s: str) -> int:
        obj = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0

        for i in range(len(s) - 1):
            if obj[s[i]] >= obj[s[i + 1]]:
                result += obj[s[i]]
            else:
                result -= obj[s[i]]

        result += obj[s[-1]]

        return result