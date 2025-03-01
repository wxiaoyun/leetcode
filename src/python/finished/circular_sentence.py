# https://leetcode.com/problems/circular-sentence/

# O(n) time
# O(1) space
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
          return False
        
        for i, c in enumerate(sentence):
          if c == ' ' and sentence[i-1] != sentence[i+1]:
            return False
        return True

# O(n) time
# O(n) space
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        n = len(words)

        for i in range(n):
          j = (i + 1) % n
          if words[i][-1] != words[j][0]:
            return False
        return True