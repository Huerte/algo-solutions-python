# Keyboard Row

class Solution(object):
    def findWords(self, words):
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        arr = []
        for word in words:
            cur = None
            for c in word.lower():
                if not cur:
                    if c in row1:
                        cur = 1
                    elif c in row2:
                        cur = 2
                    elif c in row3:
                        cur = 3
                if cur == 1 and c not in row1:
                    cur = None
                    break
                if cur == 2 and c not in row2:
                    cur = None
                    break
                if cur == 3 and c not in row3:
                    cur = None
                    break
            if cur:
                arr.append(word)
        return arr

s = Solution()
print(s.findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"])) # ["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]
print(s.findWords(["Hello","Alaska","Dad","Peace"]))       # ["Alaska","Dad"]
print(s.findWords(["adsdf","sfd"]))                        # ["adsdf","sfd"]
