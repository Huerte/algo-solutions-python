// Problem: Valid Parentheses
// Source: https://leetcode.com/problems/valid-parentheses/
// Note: Use an array as a stack and a lookup object to match closing brackets
// Time: O(n), Space: O(n)

// A string of brackets is valid when every closing bracket matches the most
// recent unmatched opening bracket. That "most recent" rule is exactly what a
// stack gives you, so this is a port of solutions/python/practice409.py with
// TypeScript type annotations added to the function and its data structures.
function isValid(s: string): boolean {
  const matchingOpen: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  const stack: string[] = [];

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

const cases: Array<[string, boolean]> = [
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
    throw new Error(`Failed for input: ${value}`);
  }
}

console.log(`All ${cases.length} test cases passed!`);
