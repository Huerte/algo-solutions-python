# HackerRank - Merge the Tools!

def merge_the_tools(string, k):
    pairs = []
    
    i = 0
    while i < len(string):
        temp = ''
        if (i + k) >= len(string):
            temp = string[i:]
        else:
            temp = string[i:i+k]
        
        seen = []
        for c in temp:
            if seen and c in seen:
                continue
            seen.append(c)
        pairs.append(''.join(seen))
        
        i += k
        
    return '\n'.join(pairs)

print(merge_the_tools('AABCAAADA', 3)) # AB\nCA\nAD
print(merge_the_tools('AAABBBCCC', 3)) # AB\nBC\nC