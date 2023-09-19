// https://leetcode.com/problems/find-the-duplicate-number

/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
  let n = nums.length;

  for (let i = 0; i < n; i++) {
    while (nums[i] !== i + 1) {
      if (nums[i] === nums[nums[i] - 1]) {
        return nums[i];
      }
      swap(nums, i, nums[i] - 1);
    }
  }

  return -1; // Return -1 if no duplicate is found
};

function swap(arr, a, b) {
  const temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}
