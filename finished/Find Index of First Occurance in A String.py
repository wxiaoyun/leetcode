# Question cannot be found on TIPS so here is the link:
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # invalid case
        if len(needle) > len(haystack):
            return -1
        
        # looping from 0 to the last possible index of needle
        for i in range(0, len(haystack) - len(needle) + 1):
            if (haystack[i] == needle[0]):
                j = 0
                while j < len(needle):
                    if (haystack[i] == needle[j]):
                        i += 1
                        j += 1
                        if (j == len(needle)):
                            return i - len(needle)
                    else:
                        break               
        return -1