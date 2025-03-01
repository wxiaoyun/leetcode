// https://leetcode.com/problems/find-k-th-smallest-pair-distance

impl Solution {
  pub fn smallest_distance_pair(nums: Vec<i32>, k: i32) -> i32 {
    let mut nums = nums;
    nums.sort();
    let min = *nums.first().unwrap() as u32;
    let max = *nums.last().unwrap() as u32;

    let count_diff = |diff: u32| -> u32 {
      let mut count = 0;
      let mut l = 0;
      for r in 0..nums.len() {
        while l < r && ((nums[r] - nums[l]) as u32 > diff) {
          l += 1;
        }
        count += r - l;
      }
      count as u32
    };

    let mut l = 0;
    let mut r = max - min;

    while l < r {
      let m = l + (r - l) / 2;
      let count = count_diff(m);
      if count < k as u32 {
        l = m + 1;
      } else {
        r = m;
      }
    }

    l as i32
  }
}

// impl Solution {
//     pub fn smallest_distance_pair(nums: Vec<i32>, k: i32) -> i32 {
//         let mut bucket = [0;1_000_000];

//         for i in 0..nums.len() {
//           for j in (i+1)..nums.len() {
//             let diff = nums[i].abs_diff(nums[j]) as usize;
//             bucket[diff] += 1;
//           } 
//         }

//         let mut count = k;
//         for (i, &c) in bucket.iter().enumerate() {
//           if count - c <= 0 {
//             return i as i32;
//           }
//           count -= c;
//         }

//         return -1;
//     }
// }