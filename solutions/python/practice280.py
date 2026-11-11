# HackerRank - The Minion Game
# Problem: The Minion Game
# Source: https://www.hackerrank.com/challenges/the-minion-game/problem
# Note: Calculates Stuart's and Kevin's scores by counting all possible substrings starting at each character, based on whether that character is a consonant or vowel.
def minion_game(string):
    st = 0
    ke = 0
    
    for i in range(len(string)):
        score = len(string) - i
        
        if string[i] in 'AEIOU':
            ke += score
        else:
            st += score
        
    if st > ke:
        print('Stuart', st)
    elif st < ke:
        print('Kevin', ke)
    else:
        print('Draw')
