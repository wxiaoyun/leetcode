// 4 x 4 matrix
// (0,0), (3,0), (3,3), (0,3)
// (0,1), (1,3), (3,2), (2,0)
// (0,2), (2,3), (3,1), (1,0)
// (1,1), (1,2), (2,2), (2,1)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  // loop over cell in the first quadrant
  for (let r = 0; r < Math.floor(matrix.length / 2); r++) {
    for (let c = 0; c < Math.floor((matrix.length + 1) / 2); c++) {
      // perform swap among the quadrants
      let cr = r;
      let cc = c;
      const original = matrix[cr][cc];

      for (let i = 0; i < 3; i++) {
        matrix[cr][cc] = matrix[matrix.length - 1 - cc][cr];
        const temp = cr;
        cr = matrix.length - 1 - cc;
        cc = temp;
      }

      matrix[cr][cc] = original;
    }
  }
};
