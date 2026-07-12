class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        less = []
        more = []

        for ch in nums:
            if ch < 0:
                less.append(ch)
            else:
                more.append(ch)
        
        ans = []
        i = j = 0

        while i < len(less):
            ans.append(more[i])
            ans.append(less[j])
            i += 1
            j += 1

        return ans