class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V":  5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "a":4, "b":9, "c":40, "d":90, "e":400, "f":900}
        number = 0
        
        s=s.replace("IV", "a")
        s=s.replace("IX", "b")
        s=s.replace("XL", "c")
        s=s.replace("XC", "d")
        s=s.replace("CD", "e")
        s=s.replace("CM", "f")

        for i in s:
            if i in roman:
                number += roman[i]
        return number

s = 'MCMXCIV'
print(Solution().romanToInt(s))