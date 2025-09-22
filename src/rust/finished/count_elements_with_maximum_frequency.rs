impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let freq = nums
            .iter()
            .fold(std::collections::HashMap::new(), |mut prev, n| {
                match prev.get_mut(n) {
                    Some(v) => *v += 1,
                    None => {
                        prev.insert(n, 1);
                    }
                };
                prev
            });

        freq.values()
            .fold((0, 0), |(cur_freq, cur_sum), &freq| match cur_freq - freq {
                ..0 => (freq, freq),
                0 => (cur_freq, cur_sum + freq),
                1.. => (cur_freq, cur_sum),
            })
            .1
    }
}
