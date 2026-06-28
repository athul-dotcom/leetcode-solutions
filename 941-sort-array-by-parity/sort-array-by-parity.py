class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        slow = 0
        for fast in range(len(nums)):

            if nums[fast] % 2 == 0:

                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums