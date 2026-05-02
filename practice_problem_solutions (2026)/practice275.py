# HackerRank - Two Characters

def alternate(s):
    ln = []
    temp = ''.join(set(s))
    for i in range(len(temp) - 1):
        for j in range(i+1, len(temp)):
            
            new_st = ''.join(c for c in s if c == temp[i] or c == temp[j])

            valid = True
            for k in range(len(new_st) - 1):
                if new_st[k] == new_st[k + 1]:
                    valid = False
                    break

            if valid and len(new_st) > 1:
                ln.append(new_st)

    return len(max(ln, key=len)) if ln else 0

print(alternate('asdcbsdcagfsdbgdfanfghbsfdab')) # 8
print(alternate('asvkugfiugsalddlasguifgukvsa')) # 0
print(alternate('beabeefeab')) # 5