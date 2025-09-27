impl Solution {
    pub fn largest_triangle_area(points: Vec<Vec<i32>>) -> f64 {
        #[inline(always)]
        fn cross_product(points: &Vec<Vec<i32>>, i: usize, j: usize, k: usize) -> f64 {
            let (ax, ay) = (points[i][0] as f64, points[i][1] as f64);
            let (bx, by) = (points[j][0] as f64, points[j][1] as f64);
            let (cx, cy) = (points[k][0] as f64, points[k][1] as f64);

            let v_vec = ((bx - cx), (by - cy));
            let u_vec = ((ax - cx), (ay - cy));

            (u_vec.0 * v_vec.1 - u_vec.1 * v_vec.0).abs()
        }

        points
            .iter()
            .enumerate()
            .flat_map(|(i, _)| {
                points
                    .iter()
                    .enumerate()
                    .take(i + 1)
                    .map(move |(j, _)| (i, j))
            })
            .flat_map(|(i, j)| {
                points
                    .iter()
                    .enumerate()
                    .take(j + 1)
                    .map(move |(k, _)| (i, j, k))
            })
            .fold(0_f64, |largest, (i, j, k)| {
                let area = cross_product(&points, i, j, k) / 2_f64;
                area.max(largest)
            })
    }
}
