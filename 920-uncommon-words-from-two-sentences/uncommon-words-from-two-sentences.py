class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combine = s1 + " " + s2
        words = combine.split()

        freq = {}
        for char in words:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        res = []

        for word in freq:
            if freq[word] == 1:
                res.append(word)

        return res