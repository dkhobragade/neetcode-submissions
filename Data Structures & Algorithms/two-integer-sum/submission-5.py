class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for key, val in enumerate(nums):
            complement = target - val

            if complement in freq:
                return [freq[complement], key]

            freq[val] = key