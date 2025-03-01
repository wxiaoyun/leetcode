class MyCalendar:

    def __init__(self):
      self.tree = None
        

    def book(self, start: int, end: int) -> bool:
      if not self.tree:
        self.tree = SegTree(start, end)
        return True
      return self.tree.update(start, end)

class SegTree:
  def __init__(self, left: int, right: int):
    self.left = left
    self.right = right
    self.leftTree = None
    self.rightTree = None

  def update(self, left: int, right: int) -> bool:
    if right <= self.left:
      if not self.leftTree:
        self.leftTree = SegTree(left, right)
        return True 
      return self.leftTree.update(left, right)
    
    if left >= self.right:
      if not self.rightTree:
        self.rightTree = SegTree(left, right)
        return True
      return self.rightTree.update(left, right)
    
    return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)