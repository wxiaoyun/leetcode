from typing import List

# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
          trie.insert(f.split('/')[1:])
        return trie.find_roots()

class Trie:
  def __init__(self):
    self.children = {}
    self.end = False
  
  def insert(self, s: List[str], i: int = 0) -> None:
    if i >= len(s):
      self.end = True
      return None
    
    if self.end:
      # Already a root folder
      return None
    
    c = s[i]
    if c not in self.children:
      self.children[c] = Trie()
    self.children[c].insert(s, i+1)

  def find_roots(self) -> List[str]:
    def helper(node: Trie, folder: str, accum: List[str]):
      if not node:
        return
      
      if node.end:
        accum.append(folder)
        return
      
      for k, n in node.children.items():
        if n:
          helper(n, folder+"/"+k, accum)
    
    result = []
    helper(self, "", result)
    return result