// Problem: Calculate Alternating Digit Sum
// Source: https://leetcode.com/problems/alternating-digit-sum/
// Note: Add and subtract consecutive digits from left to right.
// Ported from: python/practice101.py
// Time: O(d), where d is the number of digits.

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter a positive integer: ', (input) => {
  const n = input.trim();

  let plus = true;
  let res = 0;

  for (const digit of n) {
    const num = parseInt(digit, 10);
    res += plus ? num : -num;
    plus = !plus;
  }

  console.log(`Sum: ${res}`);
  rl.close();
});
