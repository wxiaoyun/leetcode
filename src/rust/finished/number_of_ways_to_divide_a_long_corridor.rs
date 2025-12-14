impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        let mut seat_cnt = 0;
        let mut plnt_cnt = 0;

        const modd: i64 = 1_000_000_007;
        let mut ways = 1;
        for c in corridor.chars() {
            match c {
                'P' => plnt_cnt += 1,
                'S' => {
                    if seat_cnt < 2 {
                        seat_cnt += 1;
                        plnt_cnt = 0;
                        continue;
                    }

                    ways = (ways * (plnt_cnt + 1)) % modd;
                    seat_cnt = 1;
                    plnt_cnt = 0;
                }
                _ => unreachable!(),
            }
        }

        if seat_cnt == 2 {
            ways as i32
        } else {
            0
        }
    }
}
