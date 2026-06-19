class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for n in nums:
            if (len(str(n)) % 2 == 0):
                count +=1
        return count