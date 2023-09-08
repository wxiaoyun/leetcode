/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  return iter([[1]], 0, numRows);
};

function iter(triangle, count, numRows) {
  if (count === numRows - 1) {
    return triangle;
  }

  const newRow = count + 1;
  triangle[newRow] = [];

  for (let i = newRow; i >= 0; i--) {
    triangle[newRow][i] =
      (triangle[count][i] ? triangle[count][i] : 0) +
      (i > 0 ? triangle[count][i - 1] : 0);
  }

  return iter(triangle, newRow, numRows);
}
