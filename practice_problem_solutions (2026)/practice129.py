# CodeWars - Simple Encryption #1 - Alternating Split

def encrypt(encrypted_text, n):
    res = encrypted_text
    for _ in range(n):

        odd = []
        even = []

        for i in range(len(res)):
            if i % 2 == 0:
                even.append(res[i])
            else:
                odd.append(res[i])

        res = ''.join(odd + even)

    return res
    
def decrypt(encrypted_text, n):
    res = encrypted_text
    for _ in range(n):
        half = len(res) // 2
        
        odd = res[:half]
        even = res[half:]
        
        temp = []
        
        for i in range(len(odd)):
            temp.append(even[i])
            temp.append(odd[i])
        
        if len(even) > len(odd):
            temp.append(even[-1])
        
        res = ''.join(temp)
    
    return res

print(encrypt("This is a test!", 0)) # This is a test!
print(encrypt("This is a test!", 1)) # hsi  etTi sats!
print(encrypt("This is a test!", 2)) # s eT ashi tist!

print(decrypt("This is a test!", 0)) # This is a test!
print(decrypt("hsi  etTi sats!", 1)) # This is a test!
print(decrypt("s eT ashi tist!", 2)) # This is a test!