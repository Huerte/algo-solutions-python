# Count Beautiful Days in a Range
# Problem: Beautiful Days at the Movies
# Source: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Note: Counts numbers in a range whose difference from their reverse is divisible by a given divisor.
st = int(input('Enter start: '))
end = int(input('Enter end: '))
div = int(input('Enter divisor: '))

res = 0

for i in range(st, end):
    temp = ((i - int(str(i)[::-1])) / div)
    if temp == int(temp):
        res += 1

print(f"The number of just right number is: {res}")
