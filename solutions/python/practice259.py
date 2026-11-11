# Count Items Matching a Rule
# Problem: Count Items Matching a Rule
# Source: https://leetcode.com/problems/count-items-matching-a-rule/
# Note: Uses a dictionary to map rule keys to item indices and counts items whose corresponding attribute matches the given rule value.
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
