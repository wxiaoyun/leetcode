// https://leetcode.com/problems/coin-change/

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
	const dp = new Array(amount + 1).fill(Number.MAX_VALUE);
	dp[0] = 0;

	for (let i = 0; i <= amount; i++) {
		for (let j = 0; j < coins.length; j++) {
			if (i - coins[j] < 0) continue;

			if (dp[i] > dp[i - coins[j]] + 1) {
				dp[i] = dp[i - coins[j]] + 1;
			}
		}
	}

	return dp[amount] === Number.MAX_VALUE ? -1 : dp[amount];
};
