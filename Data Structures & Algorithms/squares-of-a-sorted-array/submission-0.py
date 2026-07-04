class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left = 0
        right = n - 1
        post = n - 1

        while left <= right :
            if abs(nums[left]) < abs(nums[right]):
                ans[post] = nums[right] * nums[right]
                right -=1
            else:
                ans[post] = nums[left] * nums[left]
                left +=1
            post -=1
        return ans


