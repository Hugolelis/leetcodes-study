class Solution:
    def isValid(self, s: str) -> bool:
        "O(n)"
        pares = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c in pares:
                stack.append(c)
            else:
                if not stack or c != pares[stack.pop()]:
                    return False

        return not stack

print(Solution.isValid(Solution(), "(())[]{}"))
