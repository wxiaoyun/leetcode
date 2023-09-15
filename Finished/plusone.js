// https://leetcode.com/problems/plus-one/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  let index = digits.length - 1;

  while (index >= 0) {
    digits[index]++;

    if (digits[index] < 10) return digits;

    digits[index] = 0;
    index--;
  }

  digits.unshift(1);

  return digits;
};
