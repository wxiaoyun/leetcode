// https://leetcode.com/problems/daily-temperatures/

/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
  const answer = new Array(temperatures.length).fill(0);
  const stack = [temperatures.length - 1];

  for (let i = temperatures.length - 1; i >= 0; i--) {
    while (stack.length > 0) {
      const v = temperatures[stack.at(-1)];

      if (v > temperatures[i]) {
        answer[i] = stack.at(-1) - i;
        break;
      } else {
        stack.pop();
      }
    }
    stack.push(i);
  }

  return answer;
};

// /**
//  * @param {number[]} temperatures
//  * @return {number[]}
//  */
// var dailyTemperatures = function(temperatures) {
//     const answer = new Array(temperatures.length).fill(0);

//     for (let i = 0; i < temperatures.length; i++) {
//         for (let j = i; j < temperatures.length; j++) {
//             if (temperatures[j] <= temperatures[i]) continue
//             answer[i] = j-i
//             break
//         }
//     }

//     return answer
// };
