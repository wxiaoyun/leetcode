impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        bank.iter()
            .fold((0, 0), |(beams, pcnt), row| {
                let laser_cnt = row
                    .chars()
                    .fold(0, |prev, ch| prev + if ch == '1' { 1 } else { 0 });
                if laser_cnt == 0 {
                    return (beams, pcnt);
                }

                (beams + pcnt * laser_cnt, laser_cnt)
            })
            .0
    }
}
