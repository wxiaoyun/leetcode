/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
	let solution = [];

	function helper(opened, closed, current) {
		if (opened === n && closed === n) {
			solution.push(current);
			return;
		}

		if (opened < n) {
			helper(opened + 1, closed, current + "(");
		}

		if (opened > closed && closed < n) {
			helper(opened, closed + 1, current + ")");
		}
	}

	helper(0, 0, "");
	return solution;
};
