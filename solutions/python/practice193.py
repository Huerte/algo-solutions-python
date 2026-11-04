# Ho Ho Ho with Functions!
# Problem: Ho Ho Ho with Functions!
# Source: https://www.codewars.com/kata/52af1f150fcae8d33d0009bc
# Note: Uses a function with a default argument and nested function calls to generate repeated "Ho" greetings.
def ho(x = None):
    if not x:
        return "Ho!"
    return "Ho " + x

print(ho())             # Ho!
print(ho(ho(ho())))     # Ho Ho Ho!
print(ho(ho(ho(ho())))) # Ho Ho Ho Ho!
