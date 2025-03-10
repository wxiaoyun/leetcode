# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        vowels = "aeiou"
        vcnt = {v: 0 for v in vowels}
        ccnt = 0

        nxt_c = [-1] * N
        nxt = N
        for i in reversed(range(N)):
            nxt_c[i] = nxt
            if not word[i] in vcnt:
                nxt = i

        total = 0
        l = 0
        for r, ch in enumerate(word):
            if ch in vcnt:
                vcnt[ch] += 1
            else:
                cq.append(r)
                ccnt += 1

            while ccnt > k:
                c = word[l]
                if c in vcnt:
                    vcnt[c] -= 1
                else:
                    ccnt -= 1
                l += 1

            while ccnt == k and min(vcnt.values()) > 0:
                total += nxt_c[r] - r

                ch = word[l]
                if ch in vcnt:
                    vcnt[ch] -= 1
                else:
                    ccnt -= 1
                l += 1

        return total
