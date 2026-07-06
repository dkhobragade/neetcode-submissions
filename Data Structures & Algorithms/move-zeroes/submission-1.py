class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i],nums[slow] = nums[slow],nums[i]
                slow +=1