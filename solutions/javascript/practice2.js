// Problem: Calculate Alternating Digit Sum
// Source: https://leetcode.com/problems/alternating-digit-sum/
// Ported from: python/practice101.py
// Read the digits from left to right, adding the first, subtracting the next,
// and continuing to alternate. For example, 521 becomes 5 - 2 + 1 = 4.
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
    const num = parseInt(digit);
    res += plus ? num : -num;
    plus = !plus;
  }

  console.log(`Sum: ${res}`);
  rl.close();
});
