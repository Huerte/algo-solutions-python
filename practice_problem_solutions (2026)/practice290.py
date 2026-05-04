# CodeWars - Add Fractions

from fractions import Fraction
def add_fracs(*args):
    return str(Fraction(sum(eval(c) for c in args)).limit_denominator()) if args else ''

print(add_fracs())                    # ''
print(add_fracs('1/2', '3/4'))        # '5/4'
print(add_fracs('1/2', '1/3', '1/4')) # '13/12'
