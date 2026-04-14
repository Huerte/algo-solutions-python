# Count Items Matching a Rule

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        matches = 0
        rules = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                matches += 1
        return matches
    
s = Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")) # 1
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")) # 2
