// https://leetcode.com/problems/evaluate-reverse-polish-notation/

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const stack = [];

  const operators = new Set(["+", "-", "*", "/"]);

  for (const t of tokens) {
    if (operators.has(t)) {
      const e1 = stack.pop();
      const e2 = stack.pop();
      stack.push(eval(e2, e1, t));
      continue;
    }

    stack.push(Number(t));
  }

  return stack.pop();
};

function eval(e1, e2, op) {
  switch (op) {
    case "+":
      return e1 + e2;
    case "-":
      return e1 - e2;
    case "*":
      return e1 * e2;
    case "/":
      return e1 / e2 > 0 ? Math.floor(e1 / e2) : Math.ceil(e1 / e2);
    default:
      console.log(e1, e2, op);
      return NaN;
  }
}
