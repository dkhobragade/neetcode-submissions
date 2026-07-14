class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        temp = 0
        maxCount = 0

        for num in nums:
            if num == 1:
                temp +=1
            else:
                maxCount = max(maxCount,temp)
                temp =0
        return max(maxCount,temp)