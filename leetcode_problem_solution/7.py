class Solution(object):
    def intToRoman(self, num):
        roman_int_val = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000,
        }

        num_list = []

        while num > 0:
            num_list.append(num % 10)
            num //= 10

        num_list = num_list.sort(reverse=True)

        result = 0

        for i in range(len(num_list) - 1, 1, -1):
            if roman_int_val[num_list[i]] > roman_int_val[num_list[i - 1]]:
                result += roman_int_val[num_list[i]] - roman_int_val[num_list[i - 1]]
                i -= 1
            else:
                result += roman_int_val[num_list[i]]

        return result


sol = Solution()
print(sol.intToRoman(10))