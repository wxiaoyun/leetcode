#include <vector>

using namespace std;

// https://leetcode.com/problems/zero-array-transformation-i

class Solution {
 public:
  bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
    int n = nums.size();
    auto prefix_delta = vector<int>(n + 1, 0);
    for (const auto& q : queries) {
      prefix_delta[q[0]] -= 1;
      prefix_delta[q[1] + 1] += 1;
    }

    int cur_delta = 0;
    for (int i = 0; i < n; i++) {
      cur_delta += prefix_delta[i];
      if ((nums[i] + cur_delta) > 0) return false;
    }
    return true;
  }
};
