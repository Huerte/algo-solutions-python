# CodeWars - FizzBuzz++

from math import gcd, prod
def fizzbuzz_plusplus(nums, words):
    arr = []
    for i in range(1, prod(nums) + 1):
        temp = ""
        for j in range(len(nums)):
            if i % nums[j] == 0:
                temp += words[j]
        if temp:
            arr.append(temp)
        else:
            arr.append(i)
                    
    return arr

print(fizzbuzz_plusplus([2, 3, 5, 7], ["Fizz", "Buzz", "Bang", "Boom"])) # [1, 'Fizz', 'Buzz', 'Fizz', 'Bang', 'FizzBuzz', 'Boom', 'Fizz', 'Buzz', 'FizzBang', 11, 'Fizz', 13, 'FizzBuzz', 'Bang', 'FizzBoom', 17, 'Fizz', 'Buzz', 'Fizz', 'Bang', 'FizzBuzzBoom']
print(fizzbuzz_plusplus([2, 3, 5], ["Fizz", "Buzz", "Bang"]))            # [1, 'Fizz', 'Buzz', 'Fizz', 'Bang', 'FizzBuzz', 7, 'Fizz', 'Buzz', 'FizzBang', 11, 'Fizz', 13, 'FizzBuzz', 'Bang']
print(fizzbuzz_plusplus([3, 5], ["Fizz", "Buzz"]))                       # [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']