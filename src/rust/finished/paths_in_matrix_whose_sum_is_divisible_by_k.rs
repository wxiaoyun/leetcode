impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let m = grid.len() as usize;
        let n = grid[0].len() as usize;
        let mut dp = vec![vec![0i32; k]; n];
        let mut tmp = vec![vec![0i32; k]; n];
        dp[n - 1][0] = 1;
        const modd: i32 = (1e9 as i32) + 7;

        for r in (0..m).rev() {
            let r = r as usize;
            for c in (0..n).rev() {
                let c = c as usize;
                let cell_val = grid[r][c] as usize;
                for l in 0..k {
                    let m = (cell_val + l).rem_euclid(k);
                    tmp[c][m] = {
                        let prev_row_cnt = dp[c][l];
                        let prev_col_cnt = if c + 1 < n { tmp[c + 1][l] } else { 0 };
                        (prev_row_cnt + prev_col_cnt).rem_euclid(modd)
                    }
                }
            }
            std::mem::swap(&mut dp, &mut tmp);
        }

        dp[0][0]
    }
}
