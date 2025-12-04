impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let mut collisions = 0;
        let mut obstacles = 0;
        for d in directions.chars() {
            match d {
                'L' if obstacles > 0 => {
                    collisions += 1;
                }
                'L' => (),
                _ => {
                    obstacles += 1;
                }
            }
        }

        obstacles = 0;
        for d in directions.chars().rev() {
            match d {
                'R' if obstacles > 0 => {
                    collisions += 1;
                }
                'R' => (),
                _ => {
                    obstacles += 1;
                }
            }
        }

        collisions
    }
}
