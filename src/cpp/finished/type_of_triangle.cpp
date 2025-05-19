#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

// https://leetcode.com/problems/type-of-triangle

class Solution {
 public:
  string triangleType(vector<int>& nums) {
    if (nums.size() != 3) return "none";
    for (int i = 0; i < 3; i++) {
      int a = nums[i];
      int b = nums[(i + 1) % 3];
      int c = nums[(i + 2) % 3];

      if (a >= (b + c)) return "none";
    }

    auto sides = unordered_set<int>();
    for (auto n : nums) {
      sides.insert(n);
    }

    switch (sides.size()) {
      case 1:
        return "equilateral";
      case 2:
        return "isosceles";
      default:
        return "scalene";
    }
  }
};