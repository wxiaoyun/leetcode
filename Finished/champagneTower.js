// https://leetcode.com/problems/champagne-tower/

/*
      00
    10, 11
  20, 21, 22
30, 31, 32, 33
*/

/**
 * @param {number} poured
 * @param {number} query_row
 * @param {number} query_glass
 * @return {number}
 */
var champagneTower = function(poured, query_row, query_glass) {
  const tower = [[poured]]; // start pouring from the top

  for (let r = 0; r < query_row; r++) {
    for (let c = 0; c <= r; c++) {
      const overflow = Math.max(0, (tower[r][c] - 1) / 2);

      if (tower[r + 1] === undefined) tower[r + 1] = [];
      if (tower[r + 1][c] === undefined) tower[r + 1][c] = 0;
      if (tower[r + 1][c + 1] === undefined) tower[r + 1][c + 1] = 0;

      tower[r + 1][c] += overflow;
      tower[r + 1][c + 1] += overflow;
    }
  }

  return tower[query_row] ? Math.min(1, tower[query_row][query_glass] ?? 0) : 0;
};
// var champagneTower = function(poured, query_row, query_glass) {
//     const tower = [[0]];
//     pour(tower, poured, 0, 0)
//     console.log(tower)
//     return tower[query_row]
//      ? tower[query_row][query_glass] ?? 0
//      : 0
// };

// function pour(tower, amt, r, c) {
//     if (amt <= 0) return;
//     if (tower[r] === undefined) tower[r] = [];
//     if (tower[r][c] === undefined) tower[r][c] = 0;

//     if (tower[r][c] + amt <= 1) {
//         tower[r][c] += amt;
//     } else {
//         const excess = tower[r][c] + amt - 1;
//         tower[r][c] = 1;
//         pour(tower, excess/2, r+1, c);
//         pour(tower, excess/2, r+1, c+1);
//     }
// }
