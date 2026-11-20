# Problem: Sum of Even and Odd Numbers
# Source: 
# Note: Separately sums even and odd values from a list.


def sum_even_and_odd(values):
    even_sum = sum(value for value in values if value % 2 == 0)
    odd_sum = sum(value for value in values if value % 2 != 0)
    return even_sum, odd_sum


if __name__ == "__main__":
    values = list(map(int, input().split(",")))
    even_sum, odd_sum = sum_even_and_odd(values)

    print("Even:", even_sum)
    print("Odd:", odd_sum)

    assert sum_even_and_odd([1, 2, 3, 4]) == (6, 4)
    assert sum_even_and_odd([0, -2, 5]) == (-2, 5)
