#include <vector>

using namespace std;

// https://leetcode.com/problems/three-consecutive-odds

class Solution {
 public:
  bool threeConsecutiveOdds(vector<int>& arr) {
    int cur = 0;

    for (const auto n : arr) {
      int mask = (n % 2 == 0) ? 0 : 1;
      cur = cur << 1;
      cur = cur | mask;
      cur = cur & 0b111;

      if (cur == 0b111) {
        return true;
      }
    }

    return false;
  }
};