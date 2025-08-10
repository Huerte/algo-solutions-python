# 📜 Problem — Time Limit Validator
# Description:
# Given a time limit in HH:MM:SS format and a list of time durations, determine if all the
# durations can fit within the time limit. Return True if they fit, False otherwise.
# 
# Example:
# - Input: limit="02:30:00", times=["00:45:00", "01:00:00", "00:30:00"]
# - Output: True (total time: 2:15:00, which fits within 2:30:00)
# 
# Status: ✅ SOLVED

def is_valid(lim, lis):
    def extract_sec(s):
        a, b, c = map(int, s.split(':'))
        return a * 3600 + b * 60 + c

    time_limit = extract_sec(lim)
    
    for t in lis:
        time_limit -= extract_sec(t)

    if time_limit < 0:
        return False
    else:
        return True

# Test cases with assertions
# Test Case 1: Within limit
assert is_valid("02:30:00", ["00:45:00", "01:00:00", "00:30:00"]) == True

# Test Case 2: Exactly reaching the limit
assert is_valid("02:30:00", ["01:30:00", "01:00:00"]) == True

# Test Case 3: Exceeding the limit
assert is_valid("02:30:00", ["01:45:00", "01:00:00", "00:30:00"]) == False

# Test Case 4: No times given (should return True)
assert is_valid("01:00:00", []) == True

# Test Case 5: Single time exceeding the limit
assert is_valid("01:00:00", ["01:30:00"]) == False

# Test Case 6: Edge case (exact zero seconds remaining)
assert is_valid("00:10:00", ["00:05:00", "00:05:00"]) == True

print("All test cases passed!")
