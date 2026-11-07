# Valid Parentheses: Python, JavaScript, and Java

All three implementations solve [LeetCode 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/). They scan the input once and use a last-in, first-out stack so every closing bracket must match the most recent unmatched opening bracket.

## What felt different

- **Python:** A list is a natural stack, and a dictionary makes the closing-to-opening lookup concise. The implementation is the shortest of the three.
- **JavaScript:** An array provides the stack operations, while an object provides the lookup. The explicit empty-stack check is important because an unmatched closer must fail immediately.
- **Java:** ArrayDeque is a purpose-built stack alternative and avoids the legacy Stack class. Static typing makes the character comparisons more explicit, and the standalone test runner needs a class and main method.

## Complexity

Each implementation visits every character once. Each character is pushed and popped at most once, so time complexity is **O(n)** and auxiliary space complexity is **O(n)** in the worst case.

## Takeaway

The algorithm stays the same across languages. Most of the differences are in the standard-library stack API, lookup syntax, and the amount of scaffolding needed to run a few local examples.
