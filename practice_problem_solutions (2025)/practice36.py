from collections.abc import Iterable
from collections import Counter

def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    count = Counter(numbers)
    res = []
    
    pair = []
    for _, val in count.items():
        if pair and val in pair:
            continue
        pair.append(val)
            
    for freq in sorted(pair, reverse=True):
        temp = []
        for num in set(numbers):
            if count[num] == freq:
                temp += [num] * freq
        res += sorted(temp)
    
    return res

print(list(frequency_sorting([1, 2, 3, 4, 5])))
print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])))