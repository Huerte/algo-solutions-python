character = input()
x = int(input())
level = 1
for i in range(x):
    for s in range((x + 2) - (i + 3)):
        print(' ', end='')

    for j in range(level):
        print(character, end='')
    level += 2
    
    print()