# Problem: Sum of Ones in Binary
# Source: 
# Note: Sums binary 1-bits across characters in a string
s = "`!@#$%^&*(){}|;:<>?`!@#$%^&*(){}|;:<>?`"
result = sum([bin(ord(c))[2:].count('1') for c in s])
print(result)
