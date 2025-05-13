#include <vector>

using namespace std;

// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros

class Solution {
 public:
  long long minSum(vector<int>& nums1, vector<int>& nums2) {
    long long ltotal = 0;
    long long rtotal = 0;
    long long lzero = 0;
    long long rzero = 0;

    for (const auto n : nums1) {
      ltotal += n;
      if (n == 0) {
        lzero++;
      }
    }

    for (const auto n : nums2) {
      rtotal += n;
      if (n == 0) {
        rzero++;
      }
    }

    auto lmin = ltotal + lzero;
    auto rmin = rtotal + rzero;

    if (lmin < rmin && lzero == 0) {
      return -1;
    }

    if (rmin < lmin && rzero == 0) {
      return -1;
    }

    return lmin > rmin ? lmin : rmin;
  }
};