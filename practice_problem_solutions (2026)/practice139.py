# CodeWars - Chain me

def chain(init_val, functions):
    x = init_val
    for func in functions:
        x = func(x)
    return x