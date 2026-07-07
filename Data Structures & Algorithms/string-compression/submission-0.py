class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        char = ""

        while i < len(chars):
            count = 0

            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1

            char += chars[i]

            if count > 0:
                char += str(count + 1)

            i += 1

        for i in range(len(char)):
            chars[i] = char[i]

        return len(char)
