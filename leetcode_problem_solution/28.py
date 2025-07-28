
def backspaceStringCompare(s, t):
    s_l, t_l = [], []

    for l1 in s:
        if l1 != "#":
            s_l.append(l1)
        elif s_l:
            s_l.pop()

    for l2 in t:
        if l2 != "#":
            t_l.append(l2)
        elif t_l:
            t_l.pop()

    return s_l == t_l

s = input()
t = input()
print(backspaceStringCompare(s, t))