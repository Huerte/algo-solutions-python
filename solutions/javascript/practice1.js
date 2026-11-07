// Problem: Valid Parentheses
// Source: https://leetcode.com/problems/valid-parentheses/
// Note: Use an array as a stack and a lookup object to match closing brackets
// Time: O(n), Space: O(n)

function isValid(s) {
  const matchingOpen = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  const stack = [];

  for (const char of s) {
    if (Object.hasOwn(matchingOpen, char)) {
      if (stack.length === 0 || stack.pop() !== matchingOpen[char]) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
}

if (require.main === module) {
  const cases = [
    ["()", true],
    ["()[]{}", true],
    ["(]", false],
    ["([])", true],
    ["([)]", false],
    ["{[]}", true],
    ["", true],
    ["(", false],
    ["(((((((((())))))))))", true],
  ];

  for (const [value, expected] of cases) {
    if (isValid(value) !== expected) {
      throw new Error("Failed for input: " + value);
    }
  }

  console.log("All " + cases.length + " test cases passed!");
}

module.exports = { isValid };
