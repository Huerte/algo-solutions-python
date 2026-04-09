# CodeWars - Roman Numerals Decoder

def solution(roman : str) -> int:
    
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman):
            if romans[roman[i]] < romans[roman[i + 1]]:
                result += romans[roman[i + 1]] - romans[roman[i]]
                i += 2
                continue
        result += romans[roman[i]]
        i += 1
    return result

print(solution('XXI'))      # 21
print(solution('I'))        # 1
print(solution('IV'))       # 4
print(solution('MMVIII'))   # 2008
print(solution('MDCLIXIV')) # 1663