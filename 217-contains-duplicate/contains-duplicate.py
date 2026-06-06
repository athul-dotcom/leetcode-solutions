class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for char in nums:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for key in freq:
            if freq[key] >= 2:
                return True
        else:
            return False
