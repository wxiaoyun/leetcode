# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_splits = version1.split(".")
        v2_splits = version2.split(".")
        len1 = len(v1_splits)
        len2 = len(v2_splits)

        i = 0
        limit = max(len1, len2)
        while i < limit:
          n1 = int(v1_splits[i]) if i < len1 else 0
          n2 = int(v2_splits[i]) if i < len2 else 0
          if n1 < n2:
            return -1
          if n1 > n2:
            return 1
          i += 1
        return 0