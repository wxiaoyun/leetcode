#include <string>
#include <vector>

using namespace std;

// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii

class Solution {
 public:
  vector<string> getWordsInLongestSubsequence(vector<string>& words,
                                              vector<int>& groups) {
    auto dp = vector<vector<int>>(words.size());
    for (int i = 0; i < words.size(); i++) {
      dp[i].push_back(i);
    }

    for (int i = 0; i < words.size(); i++) {
      int best_idx = i;
      int best_size = dp[i].size();
      for (int j = 0; j < i; j++) {
        if (groups[i] == groups[j]) continue;
        if (words[i].size() != words[j].size()) continue;

        int hamming_dis = 0;
        for (int k = 0; k < words[i].size(); k++) {
          if (words[i][k] != words[j][k]) {
            hamming_dis++;
          }
          if (hamming_dis > 1) break;
        }
        if (hamming_dis != 1) continue;

        if (dp[j].size() + 1 > best_size) {
          best_idx = j;
          best_size = dp[j].size() + 1;
        }
      }

      if (best_idx != i) {
        vector<int> copy(dp[best_idx]);
        copy.push_back(i);
        dp[i] = copy;
      }
    }

    vector<int> res_idx;
    for (auto v : dp) {
      if (v.size() > res_idx.size()) {
        res_idx = v;
      }
    }
    vector<string> res;
    res.reserve(res_idx.size());
    for (const auto i : res_idx) {
      res.push_back(words[i]);
    }
    return res;
  }
};