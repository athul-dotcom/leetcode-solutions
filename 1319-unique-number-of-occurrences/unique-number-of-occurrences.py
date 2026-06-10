class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        seen = []
        for char in arr:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        
        for count in freq.values():
            if count in seen:
                return False
            seen.append(count)
        return True