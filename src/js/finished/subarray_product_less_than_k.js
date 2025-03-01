// https://leetcode.com/problems/subarray-product-less-than-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function (nums, k) {
	if (k <= 1) return 0;

	let count = 0;

	let l = 0;
	let r = 0;
	let cur_prod = 1;
	while (l <= r && r < nums.length) {
		cur_prod *= nums[r];

		while (cur_prod >= k) {
			cur_prod /= nums[l];
			l++;
		}

		count += r - l + 1;
		r++;
	}

	return count;
};
