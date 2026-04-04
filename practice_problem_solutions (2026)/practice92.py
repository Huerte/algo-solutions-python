# HackerRank - Validating Credit Card Numbers

import re

pattern = re.compile(r"^(?:[456]\d{15}|[456]\d{3}(-\d{4}){3})$")

n = int(input())
for _ in range(n):
    temp = input()
    
    is_seq = False
    arr = [num for num in temp if num.isdigit()]
    for i in range(len(arr) - 4):
        if len(set(arr[i+1:i+5])) == 1:
            is_seq = True
            break
            
    if is_seq:
        print('Invalid')
    else:
        print(('Invalid', 'Valid')[bool(pattern.match(temp))])