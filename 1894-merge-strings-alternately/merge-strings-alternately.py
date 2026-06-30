class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        store = []
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            store.append(word1[i])
            store.append(word2[i])
            
            i += 1
            j += 1

        store.append(word1[i:])
        store.append(word2[j:])

        return "".join(store)