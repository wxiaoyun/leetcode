// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

// Sliding window O(n)
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function (nums, x) {
	let target = -x,
		len = nums.length;

	for (let num of nums) target += num;

	if (target === 0) return len;

	let currSum = 0,
		maxLen = 0,
		l = 0;
	for (let r = 0; r < len; r++) {
		currSum += nums[r];

		while (l < r && currSum > target) {
			currSum -= nums[l];
			l++;
		}

		if (currSum === target) maxLen = Math.max(maxLen, r - l + 1);
	}

	return maxLen ? len - maxLen : -1;
};

// Binary Search O(nlogn)
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function (nums, x) {
	const accumLeft = new Array(nums.length);
	const accumRight = new Array(nums.length);

	for (let i = 0; i < nums.length; i++) {
		const j = nums.length - 1 - i;

		if (i === 0) {
			accumLeft[i] = nums[i];
			accumRight[j] = nums[j];
			continue;
		}

		accumLeft[i] = accumLeft[i - 1] + nums[i];
		accumRight[j] = accumRight[j + 1] + nums[j];
	}

	let minOps = Number.MAX_VALUE;

	for (let i = -1; i < accumLeft.length; i++) {
		const left = i >= 0 ? accumLeft[i] : 0;

		if (left === x) {
			minOps = Math.min(minOps, i + 1);
			continue;
		}

		const target = x - left;
		let rightIndex = -1;

		let l = 0;
		let r = accumLeft.length;
		while (l < r) {
			const mid = Math.trunc(l + (r - l) / 2);

			if (accumRight[mid] == target) {
				rightIndex = mid;
				break;
			} else if (accumRight[mid] < target) {
				r = mid;
			} else {
				l = mid + 1;
			}
		}

		if (rightIndex === -1) continue;
		if (accumRight.length - 1 - rightIndex + 1 + (i + 1) > nums.length)
			continue;

		minOps = Math.min(minOps, i + 1 + (accumRight.length - 1 - rightIndex + 1));
	}

	return minOps === Number.MAX_VALUE ? -1 : minOps;
};
