# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 1 digit: 3 strs
        # 2 digit: 30 - 3 = 27 strs (aa, bb, cc disallowed)
        # 3 digit: 300  (aax (3), bbx (3), ccx (3))
        
        nxt = {
            'a': 'b',
            'b': 'c',
            'c': 'a'
        }
        cur = ['a'] * n

        def is_happy(ls: list) -> bool:
            n = len(ls)
            for i in range(n-1):
                if ls[i] == ls[i + 1]:
                    return False
            return True

        def get_next(ls: list) -> list:
            n = len(ls)
            i = n - 1

            while True:
                if i < 0:
                    return []

                ls[i] = nxt[ls[i]]
                if ls[i] == 'a':
                    i -= 1
                else:
                    break
            
            if is_happy(ls):
                return ls
            return get_next(ls)

        if not is_happy(cur):
            cur = get_next(cur)

        for _ in range(k-1):
            cur = get_next(cur)
        return "".join(cur)