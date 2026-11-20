# Problem: Mumbling
# Source: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# Topic: String

def accum(st):
    parts = []
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        parts.append(part)
    return "-".join(parts)

assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
assert accum("Z") == "Z"
