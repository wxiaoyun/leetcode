// https://leetcode.com/problems/group-anagrams/

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const results = {};

  for (const str of strs) {
    const sorted = str.split("").sort().join("");
    if (results[sorted] === undefined) results[sorted] = [];
    results[sorted].push(str);
  }

  const output = [];
  Object.keys(results).forEach((key) => output.push(results[key]));
  return output;
};
