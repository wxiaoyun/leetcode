# https://leetcode.com/problems/parsing-a-boolean-expression/

# Single character cursor
class Cursor:
    def __init__(self, expr: str):
      self.expr = expr
      self.i = 0

    def peek(self) -> str:
      return self.expr[self.i]
    
    def advance(self) -> None:
      self.i += 1

    def consume(self) -> str:
      c = self.peek()
      self.advance()
      return c

    def isBool(self) -> bool:
      return self.peek() in "tf"
    
    def isNot(self) -> bool:
      return self.peek() == "!"

    def isAnd(self) -> bool:
      return self.peek() == "&"
    
    def isOr(self) -> bool:
      return self.peek() == "|"

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
      cursor = Cursor(expression)
      return self.parseExpr(cursor)
    
    def parseExpr(self, c: Cursor) -> bool:
      if c.isBool():
        return self.parseBool(c)
      
      if c.isNot():
        return self.parseNot(c)
      
      if c.isAnd():
        return self.parseAnd(c)

      if c.isOr():
        return self.parseOr(c)
    
    def parseBool(self, c: Cursor) -> bool:
      b = c.consume()

      match b:
        case "t":
          return True
        case "f":
          return False
        case _:
          raise Exception("Cursor is not pointing at a boolean: ", c)
    
    def parseNot(self, c: Cursor) -> bool:
      op = c.consume()
      if op != "!":
        raise Exception("Cursor is not pointing at NOT operator: ", c)
      
      bkt = c.consume()
      if bkt != "(":
        raise Exception("Cursor is not pointing at open bracket: ", c)
      
      bl = self.parseExpr(c)

      bkt = c.consume()
      if bkt != ")":
        raise Exception("Cursor is not pointing at closing bracket: ", c)
      
      return not bl

    
    def parseAnd(self, c: Cursor) -> bool:
      op = c.consume()
      if op != "&":
        raise Exception("Cursor is not pointing at AND operator: ", c)
      
      bkt = c.consume()
      if bkt != "(":
        raise Exception("Cursor is not pointing at open bracket: ", c)
      
      bl = True
      while c.peek() != ")":
        if c.peek() == ",":
          c.advance()
          continue
        bl = self.parseExpr(c) and bl # avoid boolean shortcircuiting

      bkt = c.consume()
      if bkt != ")":
        raise Exception("Cursor is not pointing at closing bracket: ", c)
      
      return bl

    def parseOr(self, c: Cursor) -> bool:
      op = c.consume()
      if op != "|":
        raise Exception("Cursor is not pointing at OR operator: ", c)
      
      bkt = c.consume()
      if bkt != "(":
        raise Exception("Cursor is not pointing at open bracket: ", c)
      
      bl = False
      while c.peek() != ")":
        if c.peek() == ",":
          c.advance()
          continue
        bl = self.parseExpr(c) or bl # avoid boolean shortcircuiting

      bkt = c.consume()
      if bkt != ")":
        raise Exception("Cursor is not pointing at closing bracket: ", c)
      
      return bl