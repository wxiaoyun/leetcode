# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        char_freq = defaultdict(int)
        word_sc = defaultdict(int)
        word_char_freq = {}

        for l in letters:
            char_freq[l] += 1

        for w in words:
            if w in word_char_freq:
                continue

            freq = defaultdict(int)
            word_char_freq[w] = freq

            for l in w:
                word_sc[w] += score[ord(l)-ord('a')]
                freq[l] += 1

        def restore(s: str):
            for c in s:
                char_freq[c]+=1
        
        def consume_if_can(s: str) -> Tuple[bool, int]:
            for k, v in word_char_freq[s].items():
                if char_freq[k] < v:
                    return False, 0
            
            for k, v in word_char_freq[s].items():
                char_freq[k] -= v
            return True, word_sc[s]
        

        def helper(i: int, accum: int) -> int:
            if i >= len(words):
                return accum

            leave = helper(i+1, accum) # skip i

            is_taken, val = consume_if_can(words[i]) # consume i
            take = helper(i+1, accum+val)
            if is_taken:
                restore(words[i])

            return max(leave, take)
            
        return helper(0, 0)
