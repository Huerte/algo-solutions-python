# Cancellable Item Transactions

def calculate(price_dict, transaction):
    stacks = {k: [] for k in price_dict}
    
    i = 0
    while i < len(transaction):
        
        if transaction[i].isdigit() or (transaction[i] == '-' and i+1 < len(transaction) and transaction[i+1].isdigit()):
            num_str = ''
            
            if transaction[i] == '-':
                num_str += '-'
                i += 1
            
            while i < len(transaction) and transaction[i].isdigit():
                num_str += transaction[i]
                i += 1
            
            num = int(num_str)
            item = transaction[i]
            
            stacks[item].append(num * price_dict[item])
        
        elif transaction[i].isalpha():
            item = transaction[i]
            if stacks[item]:
                stacks[item].pop()
        
        i += 1
    
    return sum(sum(v) for v in stacks.values())

print(calculate({"A":1,"B":3,"C":2}, "1A2BA3AC4CA"))        # 14
print(calculate({"X":0,"Y":0,"Z":0},'5X6Y20Z1X6Y'))         # 0
print(calculate({"R":1,"Q":2,"E":3,"X":4},"4R1Q4X2E1R2X"))  # 37
print(calculate({"T":12,"F":6},"2F5T1T"))                   # 84