# Problem: Build Tower
# Source: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# Topic: String, Formatting
# Status: IN PROGRESS

def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        spaces = " " * (n_floors - i)
        stars = "*" * (2 * i + 1)
        tower.append(spaces + stars + spaces)
    return tower

assert tower_builder(1) == ["*"]
assert tower_builder(2) == [" * ", "***"]
assert tower_builder(3) == ["  *  ", " *** ", "*****"]
