class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Invariant, i <= j < len(str)
        i, j = 0, 0

        # Keep tracks of count of occurances for characters appeared between i, j
        # Record<char, int>
        occurance_count = {}
        max_char_count = 1

        longest_substring = 1
        occurance_count[s[0]] = 1

        while i < len(s) and j < len(s):
            str_slice_len = j - i + 1

            # Not enough replacement character
            if max_char_count + k < str_slice_len:
                occurance_count[s[i]] -= 1
                if occurance_count[s[i]] == 0:
                    del occurance_count[s[i]]
                # Move i ptr right
                i += 1
                continue
            
            # Else we can update the longest substring
            longest_substring = max(longest_substring, str_slice_len)
            # Move on to the next char
            j += 1
            if j >= len(s):
                break
            if not s[j] in occurance_count:
                occurance_count[s[j]] = 0
            occurance_count[s[j]] += 1
            
            if occurance_count[s[j]] > max_char_count:
                max_char_count = occurance_count[s[j]]
        
        return longest_substring