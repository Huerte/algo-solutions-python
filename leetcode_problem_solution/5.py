class Solution1(object):
    def fib(self, n):
        base_fib = [0, 1]
        right = 1

        while len(base_fib) <= n:
            base_fib.append(base_fib[right - 1] + base_fib[right])
            right += 1
        print(base_fib)

        return base_fib[n]

class Solution2(object):
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

sol1 = Solution1()
sol2 = Solution2()
print(sol1.fib(5))
print(sol2.fib(5))