# HackerRank - Company Logo

from collections import Counter
if __name__ == '__main__':
    s = input()
    
    arr = Counter(s)
    srt = sorted(arr, key=lambda x: (-arr[x], x))[:3]
    
    for ch in srt:
        print(ch, arr[ch])

