class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        maxE = -1

        n = len(arr)

        for i in range(n-1,-1,-1):
            
            if arr[i] > maxE:
                temp = arr[i]
                arr[i] = maxE
                maxE = max(maxE,temp)
            else:
                arr[i] = maxE
        
        return arr