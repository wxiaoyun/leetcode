/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */
function longestCommonPrefix(strs: string[]): string {
  let commonPrefix = "";
  let pointer = 0;
  while (true) {
    for (let i = 0; i < strs.length; i++) {
      const str = strs[i];

      if (pointer >= str.length) return commonPrefix;

      if (str[pointer] === undefined) {
        return commonPrefix;
      }

      if (strs[0][pointer] !== str[pointer]) {
        return commonPrefix;
      }
    }
    commonPrefix += strs[0][pointer++];
  }
}
