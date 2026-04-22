# HackerRank - Drawing Book

def pageCount(n, p):
    pages = [[i, i+1] for i in range(0, n+1, 2)]
    
    cur_min = 0
    for i in range(len(pages)):
        if p in pages[i]:
            cur_min = i
    
    for i, page in enumerate(pages[::-1]):
        if p in page:
            cur_min = min(cur_min, i)
    
    return(cur_min)

print(pageCount(5, 3)) # 1
print(pageCount(6, 2)) # 1
print(pageCount(5, 4)) # 0
