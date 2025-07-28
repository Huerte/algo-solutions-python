def clearDigits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.pop()
        else:
            result.append(char)

    return ''.join(result)

print(clearDigits("a1bc2d3"))