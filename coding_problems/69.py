# Sum of ones

s = "`!@#$%^&*(){}|;:<>?`!@#$%^&*(){}|;:<>?`"
result = sum([bin(ord(c))[2:].count('1') for c in s])
print(result)