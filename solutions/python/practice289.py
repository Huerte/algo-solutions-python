# HackerRank - Angry Professor
# Problem: Angry Professor
# Source: https://www.hackerrank.com/challenges/angry-professor/problem
# Note: Determines whether class is cancelled based on whether fewer than k students arrive on time.
def angryProfessor(k, a):
    return ['NO', 'YES'][len([st for st in a if st <= 0])<k]

print(angryProfessor(3, [-1,-3,4,2])) # YES
print(angryProfessor(2, [0,-1,2,1]))  # NO
