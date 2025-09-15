impl Solution {
  pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
      let bad_mask = broken_letters.chars().fold(0_u32, |prev, cur| {
          prev | 1 << (cur as u8) as u32
      });

      text
          .split_ascii_whitespace()
          .map(|w| w.chars().fold(0_u32, |prev, cur| {
              prev | 1 << (cur as u8) as u32
          }))
          .map(|mask| {
              match mask & bad_mask {
                  0 => 1,
                  _ => 0,
              }
          })
          .sum()
  }
}