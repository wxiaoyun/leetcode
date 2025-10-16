impl Solution {
  pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
      nums.iter()
          .fold(vec![0; value as usize], |mut cs, n| {
              let class = n.rem_euclid(value);
              cs[class as usize] += 1;
              cs
          })
          .iter()
          .enumerate()
          .fold(i32::MAX, |mex, (class, &size)| {
              mex.min(size * value + class as i32)
          })
  }
}
