class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = n * (n + 1) // 2
        present_tot = sum(nums)
        find = tot - present_tot
        return find