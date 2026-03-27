# Is Prime Number

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def test_isPrime():
    """Test the isPrime function with various test cases."""
    # Test cases to verify correctness
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
                 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
                 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
                 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
                 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
                 353, 359, 367, 373, 379, 383, 389]
    numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 27, 28, 30, 32, 36]
    print("PRIMES")
    for num in prime:
        assert is_prime(num), f"Failed for {num}"
        print(f"Test passed for {num}")
    
    print("NON")
    for num in numbers:
        assert is_prime(num) == False
        print(f"Test passed for {num}")

test_isPrime()