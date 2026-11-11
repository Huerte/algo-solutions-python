# Problem: A Number After a Double Reversal
# Source: https://leetcode.com/problems/a-number-after-a-double-reversal/

#Checks whether an integer remains the same after reversing its digits twice.

#Returns False when reversing twice changes the original number, such as 120 -> 021(12) -> 12.
#Returns True when the final number matches the original number, such as 123 -> 321 -> 123.

# Then, Time Complexity become O(d), where d is the number of digits in the integer.

n = int(input('Enter an integer: '))
temp = n
for i in range(2):
    temp = int(str(temp)[::-1])

if temp == n:
    print(True)
else:
    print(False)