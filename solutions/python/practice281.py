# HackerRank - The Minion Game

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
