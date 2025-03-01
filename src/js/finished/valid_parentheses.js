// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  function getComp(bracket) {
    switch (bracket) {
      case "(":
        return ")";
      case "[":
        return "]";
      case "{":
        return "}";
      default:
        return "";
    }
  }

  function isOpeningBracket(s) {
    return s === "(" || s === "[" || s === "{";
  }

  const stack = [];

  for (const b of s) {
    if (isOpeningBracket(b)) {
      stack.push(b);
      continue;
    }

    if (stack.length === 0) return false;

    const top = stack.pop();

    if (b !== getComp(top)) return false;
  }

  return stack.length === 0;
};
