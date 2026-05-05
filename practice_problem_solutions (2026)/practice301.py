# HackerRank - Pair of gloves

from collections import Counter
def number_of_pairs(gloves):
    count = Counter(gloves)
    
    tot = []
    
    for c, v in count.items():
        pairs = v // 2
        if pairs > 0:
            tot.append([c, pairs])

    return sum(pair for _, pair in tot) if tot else 0

print(number_of_pairs(["red", "red", "red", "red", "red", "red"]))  # 3
print(number_of_pairs(["red", "green", "red", "blue", "blue"]))     # 2
print(number_of_pairs(["red", "green", "blue"]))                    # 0