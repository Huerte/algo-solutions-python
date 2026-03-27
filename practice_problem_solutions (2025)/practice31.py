import random
start = 65#32
end = 90#126
def generate_palindrome_ascii(min_chars=16, max_chars=30):
    while True:
        # ensure half length so final length > 100 (7 * chars * 2)
        half_chars = random.randint(min_chars, max_chars)

        left_half = [chr(random.randint(start, end)) for _ in range(half_chars)]
        left_bin = ''.join(format(ord(c), '07b') for c in left_half)

        palindrome_bin = left_bin + left_bin[::-1]

        # must be even and > 100
        if len(palindrome_bin) % 2 == 0 and len(palindrome_bin) > 100:
            chunks = [palindrome_bin[i:i+7] for i in range(0, len(palindrome_bin), 7)]

            try:
                full_str = ''.join(chr(int(chunk, 2)) for chunk in chunks)
                if all(start <= ord(c) <= end for c in full_str):
                    return full_str, len(palindrome_bin)
            except ValueError:
                continue

# Example usage
s, binary_len = generate_palindrome_ascii()
print("Generated string:", repr(s))
print("Binary length:", binary_len)