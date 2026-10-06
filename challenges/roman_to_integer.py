class Solution:
    def romanToInt(self, s: str) -> int:
        "O(n)"
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res: int = 0
        ant: int = 0

        for a in s:
            atual = roman[a]

            if atual > ant:
                res += atual - 2 * ant
            else:
                res += atual

            ant = atual

        return res

print(Solution.romanToInt(Solution(), "IV"))