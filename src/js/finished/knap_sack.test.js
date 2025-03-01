// Knapsack Problem

/**
 * @param {number[]}  values
 * @param {number[]} weights
 * @param {number} capacity
 * @returns {number} The maximum value that can be stored in the knapsack
 */
function knapsack(values, weights, capacity) {
	const dp = new Array(capacity + 1).fill(0);

	for (let j = 0; j < weights.length; j++) {
		for (let i = capacity; i >= 0; i--) {
			if (i - weights[j] >= 0 && dp[i] < dp[i - weights[j]] + values[j]) {
				dp[i] = dp[i - weights[j]] + values[j];
			}
		}
	}

	return dp[capacity];
}

// Test cases
describe("Knapsack Problem", () => {
	test("Test Case 1: Basic Test", () => {
		const values = [60, 100, 120];
		const weights = [10, 20, 30];
		const capacity = 50;
		expect(knapsack(values, weights, capacity)).toBe(220);
	});

	test("Test Case 2: Empty Knapsack", () => {
		const values = [];
		const weights = [];
		const capacity = 50;
		expect(knapsack(values, weights, capacity)).toBe(0);
	});

	test("Test Case 3: Zero Capacity", () => {
		const values = [60, 100, 120];
		const weights = [10, 20, 30];
		const capacity = 0;
		expect(knapsack(values, weights, capacity)).toBe(0);
	});

	test("Test Case 4: Single Item", () => {
		const values = [60];
		const weights = [10];
		const capacity = 15;
		expect(knapsack(values, weights, capacity)).toBe(60);
	});

	test("Test Case 5: Single Item, Insufficient Capacity", () => {
		const values = [60];
		const weights = [10];
		const capacity = 5;
		expect(knapsack(values, weights, capacity)).toBe(0);
	});

	test("Test Case 6: Multiple Items, Exact Capacity", () => {
		const values = [60, 100, 120];
		const weights = [10, 20, 30];
		const capacity = 60;
		expect(knapsack(values, weights, capacity)).toBe(280);
	});

	test("Test Case 7: Multiple Items, Insufficient Capacity", () => {
		const values = [60, 100, 120];
		const weights = [10, 20, 30];
		const capacity = 5;
		expect(knapsack(values, weights, capacity)).toBe(0);
	});
});
