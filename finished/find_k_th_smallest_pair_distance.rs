// https://leetcode.com/problems/find-k-th-smallest-pair-distance

impl Solution {
    pub fn smallest_distance_pair(nums: Vec<i32>, k: i32) -> i32 {
        let mut bucket = [0;1_000_000];

        for i in 0..nums.len() {
          for j in (i+1)..nums.len() {
            let diff = nums[i].abs_diff(nums[j]) as usize;
            bucket[diff] += 1;
          } 
        }

        let mut count = k;
        for (i, &c) in bucket.iter().enumerate() {
          if count - c <= 0 {
            return i as i32;
          }
          count -= c;
        }

        return -1;
    }
}