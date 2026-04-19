# HackerRank - Sequence Equation

def permutationEquation(p):
    res = []
    for i in range(1, len(p) + 1):
        inner = p.index(i) + 1
        outer = p.index(inner) + 1
        res.append(outer)
    return res

print(permutationEquation([5,2,1,3,4])) # [4,2,5,1,3]
print(permutationEquation([4,3,5,1,2])) # [1,3,5,4,2]
print(permutationEquation([2,3,1]))     # [2,3,1]