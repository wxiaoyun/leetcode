# Valid Anagram
# Easy
# 9.2K
# 286
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        count = [0] * 26
        for i in range(0, len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for j in count:
            if j != 0: return False
        return True
            