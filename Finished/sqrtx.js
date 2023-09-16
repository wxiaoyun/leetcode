// https://leetcode.com/problems/sqrtx/solutions/

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  if (x === 1) return 1;

  let lo = 0;
  let hi = x;

  while (lo < hi) {
    const mid = lo + (hi - lo) / 2;
    const guess = square(mid);
    if (isGoodEnough(x, guess, 0.001)) {
      lo = mid;
      break;
    }

    if (guess < x) {
      lo = mid;
    } else {
      hi = mid;
    }
  }

  return Math.trunc(lo);
};

function square(x) {
  return x * x;
}

function isGoodEnough(target, actual, margin) {
  if (Abs(target - actual) < margin) {
    return true;
  }

  return false;
}

function Abs(val) {
  if (val < 0) return -val;
  return val;
}
