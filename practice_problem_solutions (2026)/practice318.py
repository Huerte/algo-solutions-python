# CodeWars - So Many Permutations!

from itertools import permutations as p
def permutations(s):
    return list(set(''.join(list(e)) for e in p(s)))

print(permutations('abcd')) # ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
print(permutations('aabb')) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
print(permutations('a'))    # ['a']