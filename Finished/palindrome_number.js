/**
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 */
var isPalindrome = function (x) {
  stringVersion = x.toString();
  for (let i = 0; i < stringVersion.length / 2; i++) {
    const right = stringVersion.length - 1 - i;
    if (stringVersion[i] !== stringVersion[right]) {
      return false;
    }
  }
  return true;
};
