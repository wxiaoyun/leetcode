// https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

function timeConversion(s) {
  // Write your code here
  if (s[s.length - 2] == "A") {
    if (s.startsWith("12")) {
      return "00" + s.substring(2, 8);
    }

    return s.substring(0, 8);
  } else {
    if (s.startsWith("12")) {
      return s.substring(0, 8);
    }
    return String(Number(s.substring(0, 2)) + 12) + s.substring(2, 8);
  }
}
