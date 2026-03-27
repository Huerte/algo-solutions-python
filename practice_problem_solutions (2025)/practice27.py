# # Binary Palindrome

s = input()
result = ''.join(format(ord(c), '07b') for c in s)
print(len(result) if result == result[::-1] else 'Not a palindrome')

# import random

# def generate_palindrome_ascii(min_len=20, max_len=40):
#     while True:
#         # choose even number of chars (so binary length is even × 7)
#         half_chars = random.randint(min_len, max_len) // 2

#         # generate random ASCII chars in range 32–126
#         left_half = [chr(random.randint(32, 126)) for _ in range(half_chars)]

#         # convert to binary
#         left_bin = ''.join(format(ord(c), '07b') for c in left_half)

#         # mirror the binary (not the characters!)
#         palindrome_bin = left_bin + left_bin[::-1]

#         # split into 7-bit chunks
#         chunks = [palindrome_bin[i:i+7] for i in range(0, len(palindrome_bin), 7)]

#         try:
#             # convert back to ASCII
#             full_str = ''.join(chr(int(chunk, 2)) for chunk in chunks)

#             # check all chars printable
#             if all(32 <= ord(c) <= 126 for c in full_str):
#                 return full_str, len(palindrome_bin)
#         except ValueError:
#             # invalid binary chunk (not convertible), retry
#             continue

# # Example usage
# s, binary_len = generate_palindrome_ascii()
# print("Generated string:", repr(s))
# print("Binary length:", binary_len)
