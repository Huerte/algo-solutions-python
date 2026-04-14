# Longest Substring Without Repeating Characters

def substring(s):
    words = []
    cur = ""
    for c in s:
        if c.lower() in cur:
            words.append(cur)
            cur = ""
            continue
        cur += c
    if cur:
        words.append(cur)
    
    return max(words, key=len) if words else ""

print(substring("abcaba"))
print(substring(""))