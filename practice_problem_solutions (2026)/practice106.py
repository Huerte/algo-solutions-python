# Sort the People

class Solution(object):
    def sortPeople(self, names, heights):
        people = []
        for name, height in zip(names, heights):
            people.append([name, height])
        return [name for name, _ in sorted(people, key=lambda x: -x[1])]

s = Solution()
print(s.sortPeople(["Alice", "Bob", "Charlie"], [155, 165, 160])) # ["Bob", "Charlie", "Alice"]
print(s.sortPeople(["Alice","Bob","Bob"], [155, 185, 150])) # ["Bob", "Alice", "Bob"]