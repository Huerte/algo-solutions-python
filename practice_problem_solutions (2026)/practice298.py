# HackerRank - CamelCase

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1 if s else 0

print(camelcase("oneTwoThreeFourFiveSixSevenEightNineTen"))  # 10
print(camelcase("saveChangesInTheEditor"))                   # 5
print(camelcase(""))                                         # 0