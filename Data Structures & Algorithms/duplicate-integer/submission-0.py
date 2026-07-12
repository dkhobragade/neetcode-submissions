class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}

        for ch in nums:
            if ch in freq:
                return True
            freq[ch] = 1
        return False
