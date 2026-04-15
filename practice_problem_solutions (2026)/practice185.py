# CodeWars - Help the bookseller !

def stock_list(stocklist, categories):
    
    cur = dict(zip(categories, [0] * len(categories)))
    
    for stock in stocklist:
        name, count = stock.split()
        if name[0] in cur:
            cur[name[0]] += int(count)
        
    return " - ".join(f"({cat} : {val})" for cat, val in cur.items()) if stocklist else ''