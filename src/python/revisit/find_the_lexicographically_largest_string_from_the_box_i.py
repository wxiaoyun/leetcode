# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        N = len(word)
        size = N - numFriends + 1

        best = ""
        for i in range(N):
            sl = word[i : min(i + size, N)]
            if sl > best:
                best = sl
        return best
