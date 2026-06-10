class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for char in nums:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1

        return max(freq, key=freq.get)