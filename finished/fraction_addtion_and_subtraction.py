# https://leetcode.com/problems/fraction-addition-and-subtraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        tmp = expression.replace("-", "+-")
        frac_str = tmp.split("+")

        fractions = []
        for s in frac_str:
          if s == "":
            continue
          
          top, bottom = s.split("/")
          fractions.append((
            int(top),
            int(bottom),
          ))
        
        denominator = 1
        for _, denom in fractions:
          denominator *= denom
        
        nominator = 0
        for nom, denom in fractions:
          nominator += nom * denominator // denom
        
        if abs(nominator) == denominator:
          return "1/1" if nominator > 0 else "-1/1"
        
        cur = max(nominator, denominator) // 2
        while cur > 0:
          if (
            denominator % cur == 0 and
            nominator % cur == 0
          ):
            denominator //= cur
            nominator //= cur
            cur = min(cur - 1, max(nominator, denominator) // 2)
          else:
            cur -= 1
        
        return f"{nominator}/{denominator}" if nominator != 0 else "0/1"