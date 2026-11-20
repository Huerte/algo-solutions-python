# Problem: Stock Span Problem
# Source: https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
# Topic: Stack, Arrays
# Status: IN PROGRESS

def calculate_span(price):
    n = len(price)
    span = [1] * n
    stack = []

    for i in range(n):
        while stack and price[stack[-1]] < price[i]:
            stack.pop()

        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return span

assert calculate_span([100, 80, 60, 70, 60, 75, 85]) == [1, 1, 1, 2, 1, 4, 6]
assert calculate_span([10, 4, 5, 90, 120, 80]) == [1, 1, 2, 4, 5, 1]
assert calculate_span([10, 10, 10]) == [1, 2, 3]
