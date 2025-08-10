# 📜 Problem — Filter Strings by Substring
# Description:
# Given a list of strings and a substring, return all strings from the list that contain the substring.
# The result should be returned as a newline-separated string.
# 
# Example:
# - Input: strings=["hello", "world", "hello world"], substring="lo"
# - Output: "hello\nhello world"
# 
# Status: ✅ SOLVED

def filter_strings_by_substring(strings, substring):
    if not strings or not substring:
        return ""
    
    filtered = [x for x in strings if substring in x]
    return "\n".join(filtered)

# Test cases with assertions
assert filter_strings_by_substring(["hello", "world", "hello world"], "lo") == "hello\nhello world"
assert filter_strings_by_substring(["abc", "def", "ghi"], "x") == ""
assert filter_strings_by_substring(["test", "testing", "tested"], "test") == "test\ntesting\ntested"
assert filter_strings_by_substring([], "any") == ""
assert filter_strings_by_substring(["single"], "single") == "single"
assert filter_strings_by_substring(["hello", "world"], "") == "hello\nworld"

print("All test cases passed!")