class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        ones = 0
        zeros = 0
        best = -float('inf')
        for i, ch in enumerate(s):
          if ch == '0':
            zeros += 1
          if ch == '1':
            ones += 1
          if i < N - 1:
            best = max(best, zeros - ones)

        return best + ones

    def maxScore(self, s: str) -> int:
        N = len(s)
        psum = [0] # number of zeros
        for ch in s:
          sc = psum[-1]
          if ch == '0':
            sc += 1
          psum.append(sc)
        
        best = 0
        for k in range(1, N):
          zeros = psum[k]
          ones = (N - k) - (psum[N] - psum[k])
          best = max(best, zeros + ones)

        return best