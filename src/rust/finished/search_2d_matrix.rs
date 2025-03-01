// https://leetcode.com/problems/search-a-2d-matrix/submissions/1190671896/

pub struct Mat(Vec<Vec<i32>>);

impl Mat {
    pub fn coord_to_index(&self, r: i32, c: i32) -> i32 {
        let row_len = self.0[0].len();
        row_len as i32 * r + c
    }

    pub fn index_to_coord(&self, i: i32) -> (i32, i32) {
        let row_len = self.0[0].len() as i32;
        let r = i / row_len;
        let c = i % row_len;
        (r, c)
    }

    pub fn bin_search(&self, target: i32) -> i32 {
        let mut low = 0 as i32;
        let mut high = self.0.len() as i32 * self.0[0].len() as i32 - 1;

        while low <= high {
            let mid = low + (high - low) / 2;
            let (r, c) = self.index_to_coord(mid);
            let mid_num = self.0[r as usize][c as usize];

            if mid_num == target {
                return mid;
            } else if mid_num < target {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        -1
    }
}

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        return Mat(matrix).bin_search(target) != -1;
    }
}
