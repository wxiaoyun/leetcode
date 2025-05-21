#include <vector>

using namespace std;

// https://leetcode.com/problems/set-matrix-zeroes

class Solution {
 public:
  void setZeroes(vector<vector<int>>& matrix) {
    int R = matrix.size();
    int C = matrix[0].size();
    auto row = vector<bool>(R, false);
    auto col = vector<bool>(C, false);

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (matrix[r][c] == 0) {
          row[r] = true;
          col[c] = true;
        }
      }
    }

    for (int r = 0; r < R; r++) {
      for (int c = 0; c < C; c++) {
        if (row[r] || col[c]) {
          matrix[r][c] = 0;
        }
      }
    }
  }
};