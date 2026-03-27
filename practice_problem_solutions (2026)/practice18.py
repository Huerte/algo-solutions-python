# Calculate Percentage of Letter in String

s = input('Enter a string: ').lower()
c = input('Enter a character: ').lower()

print(f'Percentage: {int(s.count(c) / len(s) * 100)}%')