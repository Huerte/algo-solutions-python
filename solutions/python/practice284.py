# Repeated String
# Problem: Repeated String
# Source: https://www.hackerrank.com/challenges/repeated-string/problem
# Note: Counts occurrences of 'a' in an infinitely repeated string using full repetitions and the remaining prefix.
def repeatedString(s, n):
    l = len(s)
    
    total = n // l
    other = n % l
    
    return (s.count('a') * total) + s[:other].count('a')

print(repeatedString('a', 1000000000000)) # 1000000000000
print(repeatedString('aba', 10))          # 7
print(repeatedString('abcac', 10))        # 4
