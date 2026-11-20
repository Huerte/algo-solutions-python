# Problem: Zigzag Conversion
# Source: https://leetcode.com/problems/zigzag-conversion/
# Topic: String
# Status: IN PROGRESS

def convert(s, numRows):
    if numRows == 1:
        return s

    rows = [""] * numRows
    cur_row = 0
    going_down = False

    for c in s:
        rows[cur_row] += c
        if cur_row == numRows - 1:
            going_down = False
        else:
            going_down = True
        cur_row += 1 if going_down else -1

    return "".join(rows)

assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("A", 1) == "A"
