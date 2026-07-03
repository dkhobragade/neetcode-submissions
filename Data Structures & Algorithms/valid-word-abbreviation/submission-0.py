class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        i = 0
        j= 0

        while len(word) > i and len(abbr) > j:
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                j+=1
                i+=1
            else:
                if abbr[j] == "0":
                    return False
                
                num = 0

                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j+=1
                i+=num
        
        return i == len(word) and j == len(abbr)