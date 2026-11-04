# CodeWars - Chain me
# Problem: Chain me
# Source: https://www.codewars.com/kata/54fb853b2c8785dd5e000957
# Note: Applies a sequence of functions to an initial value, passing each function's output to the next.
def chain(init_val, functions):
    x = init_val
    for func in functions:
        x = func(x)
    return x
