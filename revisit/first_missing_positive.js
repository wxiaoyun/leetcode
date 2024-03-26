// https://leetcode.com/problems/first-missing-positive/

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
	// O(n) time, constant space
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] < 0) nums[i] = 0;
	}

	for (let i = 0; i < nums.length; i++) {
		const index = Math.abs(nums[i]) - 1;
		if (index < 0 || index >= nums.length) continue;
		if (nums[index] > 0) nums[index] = -nums[index];
		if (nums[index] == 0) nums[index] = -(nums.length + 1);
	}

	for (let i = 0; i < nums.length; i++) {
		if (nums[i] >= 0) {
			return i + 1;
		}
	}

	return nums.length + 1;

	// O(n) time and space solution
	// const found = [undefined];
	// found[nums.length] = undefined

	// for (const num of nums) {
	//     if (num > 0 && num <= nums.length) {
	//         found[num - 1] = true;
	//     }
	// }

	// for (let i = 0; i < found.length; i++) {
	//     if (found[i] === undefined) return i + 1
	// }

	// return nums.length

	// Sort, then linear scan: O(nlogn)
	// nums.push(0)
	// nums.sort((a, b) => a - b)

	// for (let i = 0; i < nums.length ; i++) {
	//    const left = nums[i]
	//    const right = i < nums.length-1 ? nums[i+1] : Number.MAX_SAFE_INTEGER

	//    if (left >= 0 && left+1 < right) {
	//     return left+1
	//    }
	// }

	// Naive solution: O(n^2)
	// for (let i = 1; i <= nums.length+1; i++) {
	//     let found = false;
	//     for (let j = 0; j < nums.length; j++) {
	//         if (nums[j] == i) {
	//             found = true
	//             break
	//         }
	//     }
	//     if (!found) {
	//         return i
	//     }
	// }
};
