# Ho Ho Ho with Functions!

def ho(x = None):
    if not x:
        return "Ho!"
    return "Ho " + x

print(ho())             # Ho!
print(ho(ho(ho())))     # Ho Ho Ho!
print(ho(ho(ho(ho())))) # Ho Ho Ho Ho!