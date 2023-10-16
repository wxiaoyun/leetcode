//https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
  const rowInfo = [];

  for (let i = 0; i < mat.length; i++) {
    for (let j = 0; j <= mat[i].length; j++) {
      if (mat[i][j] === 1) continue;

      rowInfo.push({
        row: i,
        strength: j,
      });

      break;
    }
  }

  rowInfo.sort((a, b) => {
    if (a.strength !== b.strength) return a.strength - b.strength;
    return a.row - b.row;
  });

  return rowInfo.splice(0, k).map((info) => info.row);
};
