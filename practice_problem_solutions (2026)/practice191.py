# Count Binary Substrings

# Mine
class Solution(object):
    def countBinarySubstrings(self, s):
        count = 0
        for i in range(len(s) - 1):
            cur = [s[i]]
            for j in range(i+1, len(s)):
                if len(set(cur)) == 1 and s[j] != cur[-1]:
                    cur.append(s[j])
                elif s[j] == cur[-1] and cur.count('1') != cur.count('0'):
                    cur.append(s[j])
                else:
                    break
            if cur.count('1') == cur.count('0'):
                count += 1
                
        return count

# Efficient Solution from GPT
class Solution(object):
    def countBinarySubstrings(self, s):
        prev = 0
        curr = 1
        count = 0

        for i in range(1, len(s)):
            print(f"{s[i]} == {s[ - 1]}")
            print(prev, curr, count)
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1

        count += min(prev, curr)
        return count
    

s = Solution()
print(s.countBinarySubstrings("00110011")) # 6
print(s.countBinarySubstrings("10101"))    # 4