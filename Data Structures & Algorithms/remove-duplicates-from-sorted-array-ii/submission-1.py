class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []

        temp = ("inf")
        count = 0

        for num in nums:
            if temp ==  num and count < 1:
                count +=1
                arr.append(num)
            elif temp != num:
                temp = num
                count = 0
                arr.append(num)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)
