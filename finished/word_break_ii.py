# https://leetcode.com/problems/word-break-ii/

class Trie:
    def __init__(self, strs: List[str] = None):
        self.children = [None for i in range(26)]
        self.end = False

        if strs:
            for s in strs:
                self.add(s)

    def add(self, s: str):
        if len(s) == 0:
            self.end = True
            return
        
        c = s[0]
        index = ord(c)-ord('a')
        if not self.children[index]:
            self.children[index] = Trie()
        
        self.children[index].add(s[1:])
    
    def is_word(self, s: str) -> bool:
        return self.is_word_helper(s, 0)

    def is_word_helper(self, s: str, i: int) -> bool:
        if i == len(s):
            return self.end
        
        c = s[i]
        index = ord(c)-ord('a')
        if not self.children[index]:
            return False
        else:
            return self.children[index].is_word_helper(s, i+1)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        t = Trie(wordDict)
        result = []

        def dfs(i: int, accum: List[str]):
            if i >= len(s):
                return result.append(' '.join(accum))
            
            for j in range(i+1, len(s)+1):
                b = t.is_word(s[i:j])
                
                if not b:
                    continue
                
                # pick
                cp = copy.deepcopy(accum)
                cp.append(s[i:j])
                dfs(j, cp)

                # no pick
                # continue
        
        dfs(0, [])
        return result
