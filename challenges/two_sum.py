class Solution:
    def twoSum(self, nums: list, target: int):
        "O(n)"
        seen = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i

        return []

print(Solution.twoSum(Solution(), [1, 2, 3, 4], 3))