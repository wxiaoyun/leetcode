# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        
        for i, w in enumerate(words):
          if len(w) < len(searchWord):
            continue
          
          if searchWord == w[:len(searchWord)]:
            return i + 1
        
        return -1