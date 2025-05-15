#include <string>
#include <vector>

using namespace std;

// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i

class Solution {
 public:
  vector<string> getLongestSubsequence(vector<string>& words,
                                       vector<int>& groups) {
    vector<string> res = {words[0]};
    int next = 1 ^ groups[0];
    for (int i = 1; i < groups.size(); i++) {
      if (groups[i] == next) {
        res.push_back(words[i]);
        next ^= 1;
      }
    }

    return res;
  }
};