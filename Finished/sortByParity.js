// https://leetcode.com/problems/sort-array-by-parity/?envType=daily-question&envId=2023-09-28

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
  let even = 0;
  for (const index in nums) {
    if (nums[index] % 2 === 1) continue;

    const temp = nums[index];
    nums[index] = nums[even];
    nums[even] = temp;
    even++;
  }
  return nums;
};
