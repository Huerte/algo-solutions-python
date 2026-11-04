# HackerRank - Company Logo
# Problem: Company Logo
# Source: https://www.hackerrank.com/challenges/most-commons/problem
# Note: Finds the three most frequent characters, sorting by descending frequency and alphabetical order for ties.

from collections import Counter
if __name__ == '__main__':
    s = input()
    
    arr = Counter(s)
    srt = sorted(arr, key=lambda x: (-arr[x], x))[:3]
    
    for ch in srt:
        print(ch, arr[ch])

