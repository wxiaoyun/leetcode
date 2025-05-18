#include <functional>
#include <unordered_map>
#include <vector>

using namespace std;

// https://leetcode.com/problems/painting-a-grid-with-three-different-colors

class Solution {
 public:
  int colorTheGrid(int m, int n) {
    auto valid_perm = vector<int>();
    std::function<void(int, int)> dfs = [&](int depth, int cur) {
      if (depth == m) {
        valid_perm.push_back(cur);
        return;
      }

      for (int i = 0; i < 3; i++) {
        int color_mask = 1 << i;
        int prev_color = cur & 0b111;
        if (color_mask == prev_color) continue;
        dfs(depth + 1, (cur << 3) | color_mask);
      }
    };
    dfs(0, 0);

    auto valid_pair = unordered_map<int, vector<int>>();
    for (int p : valid_perm) {
      auto pairs = vector<int>();
      for (int op : valid_perm) {
        if ((p & op) != 0) continue;
        pairs.push_back(op);
      }
      valid_pair[p] = std::move(pairs);
    }

    auto prev_dp = unordered_map<int, long long>();
    for (int p : valid_perm) {
      prev_dp[p] = 1;
    }

    long long MOD = 1e9 + 7;
    auto dp = unordered_map<int, long long>();
    for (int r = 1; r < n; r++) {
      for (int p : valid_perm) {
        for (int op : valid_pair[p]) {
          dp[p] = (dp[p] + prev_dp[op]) % MOD;
        }
      }
      prev_dp = std::move(dp);
      dp.clear();
    }

    long long res = 0;
    for (auto pair : prev_dp) {
      res = (res + pair.second) % MOD;
    }
    return static_cast<int>(res);
  }
};