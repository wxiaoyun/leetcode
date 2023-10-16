// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  let current;
  while (left < right) {
    current = numbers[left] + numbers[right];

    if (current < target) left++;
    else if (current > target) right--;
    else return [left + 1, right + 1];
  }

  return [-1, -1];
};
