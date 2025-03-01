// https://leetcode.com/problems/longest-consecutive-sequence/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
  const occurance = {};

  for (const num of nums) occurance[num] = true;

  let max = 0;

  Object.keys(occurance).forEach((num) => {
    if (occurance[num - 1]) return;
    let count = 1;
    let cur = num;
    while (occurance[cur]) {
      max = Math.max(max, count);
      cur++;
      count++;
    }
  });

  return max;
};
