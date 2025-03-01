# https://leetcode.com/problems/replace-words/

from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def add(self, w: str):
        if len(w) == 0:
            self.end = True
            return

        c = w[0]
        r = w[1:]
        
        if not c in self.children:
            self.children[c] = Trie()

        return self.children[c].add(r)

    def find_root(self, w: str):
        def find_root_helper(t: Trie, w: str, tmp: str):
            if t.end:
                return tmp
            
            if len(w)==0:
                return ""
            
            c = w[0]
            r = w[1:]

            if c not in t.children:
                return ""
            
            return find_root_helper(t.children[c], r, tmp+c)
        
        return find_root_helper(self, w, "")

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()

        for d in dictionary:
            t.add(d)
        
        st = sentence.split(" ")

        for i in range(len(st)):
            s = st[i]
            root = t.find_root(s)
            st[i] = root if root != "" else st[i]
        
        return " ".join(st)