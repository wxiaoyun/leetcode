# https://leetcode.com/problems/number-of-atoms

from collections import defaultdict
from typing import Dict, Tuple


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def helper(f: str, start_idx: int) -> Tuple[Dict[str, int], int]:
            res = defaultdict(int)

            i = start_idx
            while i < len(f):
                j = i
                c = f[j]

                match c:
                    case "(":
                        j += 1 # consume "("
                        sub_res, j = helper(f, j)

                        multiple = 1 # default 1
                        if j < len(f) and f[j].isnumeric():
                            multiple = ord(f[j])-ord('0') # update if theres number
                            j += 1 
                        while j < len(f) and f[j].isnumeric():
                            multiple = multiple*10 + ord(f[j])-ord('0')
                            j += 1
                        
                        for e, c in sub_res.items():
                            res[e] += c*multiple
                    
                    case ")":
                        j += 1 # consume ")"
                        return res, j
        
                    case _:
                        start_str = j
                        j += 1
                        if j < len(f) and f[j].isalpha() and not f[j].isupper():
                            j += 1
                        end_str = j

                        multiple = 1
                        if j < len(f) and f[j].isnumeric():
                            multiple = ord(f[j])-ord('0')
                            j += 1
                        while j < len(f) and f[j].isnumeric():
                            multiple = multiple*10 + ord(f[j])-ord('0')
                            j += 1
                        elm = f[start_str:end_str]
                        res[elm] += multiple
                
                i = j

            return res, j
        
        result, _ = helper(formula, 0)
        count = [(elm, cnt) for elm, cnt in result.items()]
        count.sort(key=lambda x: x[0])

        result = []
        for elm, cnt in count:
            if cnt == 1:
                result.append(elm)
            else:
                result.append(elm+str(cnt))
        return "".join(result)
        