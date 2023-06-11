import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.util.ArrayList;

class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);

    Set<List<Integer>> result = new HashSet<>();

    for (int i = 0; i < nums.length; i++) {
      int left = 0;
      int right = nums.length - 1;

      while (left < right) {
        if (left == i) {
          left++;
          continue;
        }

        if (right == i) {
          right--;
          continue;
        }

        int sum = nums[left] + nums[right] + nums[i];

        if (sum == 0) {
          List<Integer> triplet = Arrays.asList(nums[left], nums[right], nums[i]);
          result.add(triplet);
          left++;
          right--;
        } else if (sum < 0) {
          left++;
        } else {
          right--;
        }
      }
    }

    List<List<Integer>> finalResult = new ArrayList<>(result);
    return finalResult;
  }
}