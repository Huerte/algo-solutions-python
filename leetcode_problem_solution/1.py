
def longestCommonPrefix(strs):
    sample_word = strs[0]

    for word in strs[1:]:
        while sample_word and word[:len(sample_word)] != sample_word:
            sample_word = sample_word[:-1]
    return sample_word

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))