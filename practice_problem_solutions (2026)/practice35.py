# String Frequency Sorter
from collections import Counter
def sort_characters_by_frequency(s):

    freq = Counter(s)
    
    return ''.join(sorted(s, key=lambda c: (-freq[c], c)))


print(sort_characters_by_frequency('cbaba'))
































def test_sort_characters_by_frequency():
    assert sort_characters_by_frequency("aabbccc") == "cccaabb"
    assert sort_characters_by_frequency("hello") == "lleho"
    assert sort_characters_by_frequency("") == ""
    assert sort_characters_by_frequency("abc") == "abc"
    assert sort_characters_by_frequency("abbbcc") == "bbbcca"

test_sort_characters_by_frequency()
print('Success')