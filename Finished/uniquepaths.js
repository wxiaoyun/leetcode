// https://leetcode.com/problems/unique-paths/
//
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  return nChooseR(m + n - 2, m - 1);
};

function nChooseR(n, r) {
  if (r <= 0 || r >= n) return 1;
  return factorial(n) / (factorial(r) * factorial(n - r));
}

function factorial(n) {
  if (n <= 1) return n;

  let result = 1;

  while (n >= 1) {
    result *= n;
    n--;
  }

  return result;
}
