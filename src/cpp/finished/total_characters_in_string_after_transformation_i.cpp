#include <cmath>
#include <functional>
#include <unordered_map>
#include <vector>

using namespace std;

// https://leetcode.com/problems/total-characters-in-string-after-transformations-i

class Solution {
 public:
  int lengthAfterTransformations(string s, int t) {
    auto age = vector<int>();
    for (const auto ch : s) {
      int n = ch - 'a' + t;
      age.push_back(n);
    }

    int cycle = 'z' - 'a' + 1;

    int MOD = static_cast<int>(pow(10, 9)) + 7;
    auto dp = unordered_map<int, int>();
    std::function<int(int)> resolve_length = [&](int age) {
      int cycles = age / cycle;
      if (cycles < 1) {
        return 1;
      }

      if (auto search = dp.find(age); search != dp.end()) {
        return search->second;
      }

      int len = resolve_length(age - cycle);
      len = (len + resolve_length(age - cycle + 1)) % MOD;

      dp.insert({age, len});
      return len;
    };

    int result = 0;
    for (const auto a : age) {
      result = (result + resolve_length(a)) % MOD;
    }
    return result;
  }
};