// Problem: Valid Parentheses
// Source: https://leetcode.com/problems/valid-parentheses/
// Note: Use ArrayDeque as a stack and match each closer against the most recent opener
// Time: O(n), Space: O(n)

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
                continue;
            }

            if (stack.isEmpty()) {
                return false;
            }

            char opening = stack.pop();
            if ((ch == ')' && opening != '(')
                    || (ch == ']' && opening != '[')
                    || (ch == '}' && opening != '{')) {
                return false;
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String[] inputs = {"()", "()[]{}", "(]", "([])", "([)]", "{[]}", "", "(", "(((((((((())))))))))"};
        boolean[] expected = {true, true, false, true, false, true, true, false, true};
        Solution solution = new Solution();

        for (int i = 0; i < inputs.length; i++) {
            if (solution.isValid(inputs[i]) != expected[i]) {
                throw new AssertionError("Failed for input: " + inputs[i]);
            }
        }

        System.out.println("All " + inputs.length + " test cases passed!");
    }
}
