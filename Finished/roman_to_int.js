/**
 * Given a roman numeral, convert it to an integer.
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const romanToIntMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let sum = 0;
  for (let i = 1; i < s.length; i++) {
    if (romanToIntMap[s[i - 1]] < romanToIntMap[s[i]]) {
      sum -= romanToIntMap[s[i - 1]];
    } else {
      sum += romanToIntMap[s[i - 1]];
    }
  }
  return sum + romanToIntMap[s[s.length - 1]];
};
