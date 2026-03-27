# Difference in Digit Sums

def calc(x):
    total1 = ''.join(map(str, [ord(c) for c in x]))
    return int(sum(map(int, total1))) - int(sum(map(int,total1.replace('7', '1'))))

print(calc("ABC"))
