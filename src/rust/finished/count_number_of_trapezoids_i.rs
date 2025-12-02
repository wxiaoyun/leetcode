impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashMap;

        let level_cnt: HashMap<_, i32> =
            points.into_iter().fold(HashMap::new(), |mut mp, point| {
                let y = point[1];
                mp.insert(y, 1i32 + mp.get(&y).copied().unwrap_or(0));
                mp
            });

        let mut total = 0i32;
        let mut prev_cand = 0i32;
        let modd = 1_000_000_007i64;
        for points in level_cnt.into_values() {
            let points = points as i64;
            let local_cand = points * (points - 1) / 2;
            total = (total as i64 + local_cand * prev_cand as i64).rem_euclid(modd) as i32;
            prev_cand += local_cand as i32;
        }

        total
    }
}
