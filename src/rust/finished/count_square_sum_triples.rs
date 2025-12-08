impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut count = 0;

        for i in (1..=n) {
            for j in (1..i) {
                let asq = i.pow(2);
                let bsq = j.pow(2);
                let csq = asq + bsq;
                let c = (csq as f64).sqrt().floor() as i32;
                if c <= n && c.pow(2) == csq {
                    count += 2;
                }
            }
        }

        count
    }
}
