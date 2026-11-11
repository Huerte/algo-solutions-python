# HackerRank - Regex Substitution
# Problem: Regex Substitution
# Source: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Note: Replaces && with and and || with or when surrounded by spaces using regular expressions.
import re

def replace(match):
    op = match.group(0)
    return "or" if op == "||" else "and"

for _ in range(int(input())):
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", replace, input()))
