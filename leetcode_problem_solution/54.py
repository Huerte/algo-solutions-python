def is_equal(s1, s2):
    if len(s1) != len(s2):
        return False

    m = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
    if not m:
        return True
    elif len(m) == 2 and m[0][1] == m[1][2] and m[0][2] == m[1][1]:
        return True

    return False


print(is_equal('bank', 'kanb'))

# Test cases for is_equal function
assert is_equal("bank", "kanb") == True  # Swapping 'b' and 'k' makes them equal
assert is_equal("abcd", "acbd") == True  # Swapping 'b' and 'c' makes them equal
assert is_equal("abcd", "abdc") == True  # Swapping 'c' and 'd' makes them equal
assert is_equal("abcd", "abcd") == True  # Already equal, should return True
assert is_equal("abcd", "abcf") == False  # More than two mismatches
assert is_equal("abcd", "ab") == False  # Different lengths
assert is_equal("abcd", "bcda") == False  # More than one swap needed
assert is_equal("aabb", "bbaa") == False  # More than one swap needed

print("All test cases passed! ✅")
