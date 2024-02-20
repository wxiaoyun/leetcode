// https://leetcode.com/problems/trapping-rain-water/

var trap = function(height) {
  const n = height.length;
  if (n === 0) return 0;

  const leftToRightMax = new Array(n).fill(0);
  const rightToLeftMax = new Array(n).fill(0);

  leftToRightMax[0] = height[0];
  rightToLeftMax[n - 1] = height[n - 1];

  let accum = 0;

  for (let i = 1, j = n - 2; i < n; i++, j--) {
    leftToRightMax[i] = Math.max(leftToRightMax[i - 1], height[i]);
    rightToLeftMax[j] = Math.max(rightToLeftMax[j + 1], height[j]);
  }

  for (let i = 0; i < n; i++) {
    accum += Math.min(leftToRightMax[i], rightToLeftMax[i]) - height[i];
  }

  return accum;
};

// /**
//  * @param {number[]} height
//  * @return {number}
//  */
// var trap = function(height) {
//     const leftToRightMax = [];
//     const rightToLeftMax = [];

//     for (let i = 0; i < height.length; i++) {
//         const opp = height.length - i - 1;

//         if (i === 0) {
//             leftToRightMax[i] = height[i];
//             rightToLeftMax[opp] = height[opp];
//             continue;
//         }

//         leftToRightMax[i] = Math.max(leftToRightMax[i-1], height[i]);
//         rightToLeftMax[opp] = Math.max(rightToLeftMax[opp+1], height[opp]);
//     }

//     let accum = 0;

//     for (let i = 0; i < height.length; i++) {
//         accum += Math.abs(Math.min(leftToRightMax[i], rightToLeftMax[i]) - height[i])
//     }

//     return accum
// };
