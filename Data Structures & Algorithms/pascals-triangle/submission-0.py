class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        temp = []

        first = [1]
        second = [1,1]

        temp.append(first)
        temp.append(second)

        j = numRows-2

        while j != 0:
            pas = []
            arr = temp[-1]
            pas.append(arr[0])
            for i in range(len(arr)):
                if i == len(arr)-1:
                    pas.append(arr[i])
                else:
                    pas.append(arr[i]+arr[i+1])
            j-=1
            temp.append(pas)
        return temp