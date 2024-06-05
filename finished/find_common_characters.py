# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cc = defaultdict(int)
        for w in words:
            c = Counter(w)
            for k, v in c.items():
                for i in range(v):
                    cc[k+str(i)] += 1

        res = []
        for k, v in cc.items():
            if v == len(words):
                res.append(k[:1])
        return res