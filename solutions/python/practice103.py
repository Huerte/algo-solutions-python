# Problem: Calculate Percentage of Letter in String
# Source: https://leetcode.com/problems/percentage-of-letter-in-string/
# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

# Input:
# - s: A string consisting of lowercase and uppercase English letters (1 <= s.length <= 100)
# - c: A character representing the target letter to count

# Output:
# - An integer representing the percentage of occurrences of c in s (floored)
#
# Examples:
# Example 1:
#   Input:  s = "foobar", letter = "o"
#   Output: 33
#   Explanation: The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down.

def letter_percentage(s, c):
    if not s:
        return 0
    return int(s.lower().count(c.lower()) / len(s) * 100)


if __name__ == "__main__":
    s = input("Enter a string: ")
    c = input("Enter a character: ")
    print(f"Percentage: {letter_percentage(s, c)}%")


# Test cases with assertions
assert letter_percentage("hello", "l") == 40
assert letter_percentage("Hello", "H") == 20
assert letter_percentage("abc", "z") == 0
assert letter_percentage("aaaa", "A") == 100
assert letter_percentage("", "a") == 0

print("All test cases passed!")
