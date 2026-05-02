# HackerRank - Fair Rations

def fairRations(B):
    count = 0
    for i in range(len(B)):
        if B[i] % 2 != 0:
            if i + 1 < len(B):
                print(B)
                B[i] += 1
                B[i + 1] += 1
                count += 2
            else:
                print(B)
                break
            print('=' * 20)
    print(B)
    if all(c % 2 == 0 for c in B):
        return count
    return 'NO'

print(fairRations([2, 3, 4, 5, 6])) # 2
print(fairRations([1, 2]))    # NO