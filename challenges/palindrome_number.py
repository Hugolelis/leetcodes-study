class Solution:
    def isPalindrome(self, x: int) -> bool:
        "O(1)"
        strNum = str(x)
        invertNum = strNum[::-1]

        return invertNum == strNum

print(Solution.isPalindrome(Solution(), 66))