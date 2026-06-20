class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []
        freq = {}
        for char in nums:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for count in freq.values():
            if count >= 2:
                return True
        else:
            return False