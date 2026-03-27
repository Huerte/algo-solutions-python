# 1000-digit Fibonacci Number
# Return the first 1000-digit fibonacci number index

a, b = 0, 1
from math import log10, ceil

i = 1
while ceil(log10(b)) < 1000:
    a, b = b, a + b
    i += 1

print(b)

print(f"\nIndex is: {i}")
print('Digit Count of "b":', len(str(b)))