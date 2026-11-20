# Problem: Letter Combinations of a Phone Number
# Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Topic: Backtracking, String

def letter_combinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    res = []

    def backtrack(idx, current):
        if idx == len(digits):
            res.append(current)
            return
        for letter in phone_map[digits[idx]]:
            backtrack(idx + 1, current + letter)

    backtrack(0, "")
    return res

assert letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert letter_combinations("") == []
assert letter_combinations("2") == ["a", "b", "c"]
assert len(letter_combinations("234")) == 27  # 3*3*3
