// https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function(inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function() {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'birthdayCakeCandles' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY candles as parameter.
 */

function birthdayCakeCandles(candles) {
  // Write your code here
  // String()

  // Create a hashmap for frequency
  const freq = {};

  candles.forEach((val) => {
    if (!freq[String(val)]) freq[String(val)] = 0;
    freq[String(val)] = freq[String(val)] + 1;
  });

  let maxKey = -1;
  for (const key in freq) {
    if (Number(key) > maxKey) maxKey = Number(key);
  }

  return freq[String(maxKey)];
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const candlesCount = parseInt(readLine().trim(), 10);

  const candles = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((candlesTemp) => parseInt(candlesTemp, 10));

  const result = birthdayCakeCandles(candles);

  ws.write(result + "\n");

  ws.end();
}
