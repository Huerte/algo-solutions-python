# CodeWars - Help the bookseller !
# Problem: Help the bookseller!
# Source: https://www.codewars.com/kata/54dc6f5a224c26032800005c
# Note: Groups book quantities by their first-letter category and returns the total stock for each requested category in the specified order.
def stock_list(stocklist, categories):
    
    cur = dict(zip(categories, [0] * len(categories)))
    
    for stock in stocklist:
        name, count = stock.split()
        if name[0] in cur:
            cur[name[0]] += int(count)
        
    return " - ".join(f"({cat} : {val})" for cat, val in cur.items()) if stocklist else ''
