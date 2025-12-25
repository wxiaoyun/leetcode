impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        let mut carry = 0;
        let mut a = a;
        let mut b = b;

        while b != 0 {
            carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }

        a
    }
}
