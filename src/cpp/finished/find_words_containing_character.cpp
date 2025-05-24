#include <string>
#include <vector>

using namespace std;

// https://leetcode.com/problems/find-words-containing-character/

class Solution {
 public:
  vector<int> findWordsContaining(vector<string>& words, char x) {
    auto res = vector<int>();

    for (int i = 0; i < words.size(); i++) {
      auto& w = words[i];
      size_t idx = w.find(x);
      if (idx != string::npos) {
        res.push_back(i);
      }
    }

    return res;
  }
};