class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for char in nums:
            if char in freq:
                freq[char] += 1
            else:
                 freq[char] = 1
        
        for num , count in freq.items():
            if count == 1:
                return num