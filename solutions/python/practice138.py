# Difference in Digit Sums
# Problem: Char Code Calculation
# Source: https://www.codewars.com/kata/char-code-calculation/
# Note: Calculates the difference between digit sums before and after replacing 7 with 1 in concatenated ASCII codes. 

def calc(x):
    total1 = ''.join(map(str, [ord(c) for c in x]))
    return int(sum(map(int, total1))) - int(sum(map(int,total1.replace('7', '1'))))

print(calc("ABC"))
