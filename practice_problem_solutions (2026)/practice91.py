# HackerRank - Regex Substitution

import re

def replace(match):
    op = match.group(0)
    return "or" if op == "||" else "and"

for _ in range(int(input())):
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace, input()))