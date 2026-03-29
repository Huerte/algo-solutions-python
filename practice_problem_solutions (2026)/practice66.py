# Count Asterisks

class Solution(object):
    def countAsterisks(self, s):
        if '*' not in s:
            return 0
        elif '|' not in s:
            return s.count('*')
        
        had_f = False
        count = 0
        for c in s:
            if c == '|':
                had_f = not had_f
            elif not had_f and c == '*':
                count += 1
        return count