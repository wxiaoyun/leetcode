function query(A, k) {
  return k === 0
    ? Number.MIN_SAFE_INTEGER
    : k > A.length
    ? Number.MAX_SAFE_INTEGER
    : A[k - 1];
}

function findMedian(A, B, n) {
  let low = 1;
  let high = n;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let a = query(A, mid);
    let b = query(B, n - mid + 1);
    let aNext = query(A, mid + 1);
    let bPrev = query(B, n - mid);

    if (a < b && bPrev < aNext) {
      return (Math.max(a, bPrev) + Math.min(aNext, b)) / 2;
    } else if (a > b) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
}

// Test the code
let A = [1, 3, 7, 10, 13];
let B = [2, 4, 6, 8, 11];

let n = A.length; // A and B should have the same length for this algorithm

console.log(findMedian(A, B, n)); // Output should be 7

// More tests
A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
B = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20];

n = A.length; // A and B should have the same length for this algorithm

console.log(findMedian(A, B, n)); // Output should be

console.log("\nTest 3");

A = [1, 2, 3, 4, 5];
B = [6, 7, 8, 9, 10];

n = A.length; // A and B should have the same length for this algorithm

console.log(findMedian(A, B, n)); // Output should be 5.5

console.log("\nTest 4");

A = [1];
B = [2];

n = A.length; // A and B should have the same length for this algorithm

console.log(findMedian(A, B, n)); // Output should be 1.5

console.log("\nTest 5");

A = [3, 4, 5];
B = [1, 2, 6];

n = A.length; // A and B should have the same length for this algorithm

console.log(findMedian(A, B, n)); // Output should be 3.5
