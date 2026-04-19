# HackerRank - 
# TODO

def permutationEquation(p):
    res = []
    print(p)
    for i in range(len(p)):
        ind = p.index(i + 1) + 1
        print(i + 1, ind, sep=' --- ')
        res.append(p[ind-1])
        # print(p.find(ind) + 1)
    return res

# print(permutationEquation([5,2,1,3,4])) # [4,2,5,1,3]
# print(permutationEquation([4,3,5,1,2])) # [1,3,5,4,2]
print(permutationEquation([2,3,1]))     # [2,3,1]