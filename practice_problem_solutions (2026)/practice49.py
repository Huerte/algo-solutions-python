# Longest Substring Without Repeating Characters

def longest_substring(s):

    words = []
    
    temp = ""
    for c in s:
        if not temp:
            temp += c
            continue
        
        if c not in temp:
            temp += c
        else:
            words.append(temp)
            temp = c

    return len(max(words, key=len))


print(longest_substring("abcabcbb")) # == 3
print(longest_substring("bbbbb"))    # == 1
print(longest_substring("pwwkew"))   # == 3
print(longest_substring("abcdac"))   # == 4