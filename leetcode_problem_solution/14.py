# Get n a number then return true if its palindrome

def isPalindrome1(n):
    extracted_n = []
    while n > 0:
        extracted_n.append(n % 10)
        n //= 10
    return extracted_n == extracted_n[::-1]

def isPalindrome2(n):
    n = str(n)
    return n == n[::-1]


print(isPalindrome1(123))
print(isPalindrome1(1001))
print(isPalindrome1(121))

print("=" * 30)

print(isPalindrome2(123))
print(isPalindrome2(1001))
print(isPalindrome2(121))
