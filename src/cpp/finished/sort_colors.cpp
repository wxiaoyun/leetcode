#include <vector>

using namespace std;

// https://leetcode.com/problems/sort-colors

class Solution {
 public:
  void sortColors(vector<int>& nums) {
    int count[] = {0, 0, 0};

    for (auto n : nums) {
      count[n]++;
    }

    int i = 0;
    for (int n = 0; n < 3; n++) {
      int cnt = count[n];
      for (int j = 0; j < cnt; j++) {
        nums[i] = n;
        i++;
      }
    }
  }
};