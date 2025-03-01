# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        output = []

        cur, count = word[0], 1
        for c in word[1:]:
          if c != cur or count >= 9:
            output.append(str(count))
            output.append(cur)
            cur = c
            count = 1
          else:
            count += 1
        
        output.append(str(count))
        output.append(cur)

        return "".join(output)
