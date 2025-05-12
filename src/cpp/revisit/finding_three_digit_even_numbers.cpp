#include <vector>

using namespace std;

class Solution {
 public:
  vector<int> findEvenNumbers(vector<int>& digits) {
    auto count = vector<int>(10);

    for (const auto d : digits) {
      count[d]++;
    }

    auto res = vector<int>();
    for (int i = 1; i < 10; i++) {
      if (count[i] == 0) {
        continue;
      }
      count[i]--;

      for (int j = 0; j < 10; j++) {
        if (count[j] == 0) {
          continue;
        }
        count[j]--;

        for (int k = 0; k < 10; k += 2) {
          if (count[k] == 0) {
            continue;
          }

          res.push_back(i * 100 + j * 10 + k);
        }
        count[j]++;
      }
      count[i]++;
    }

    return res;
  }
};