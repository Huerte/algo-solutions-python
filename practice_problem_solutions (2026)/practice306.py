# CodeWars - Count IP Addresses

def ips_between(start, end):
    return sum([int(num) * (256 ** (3 - i)) for i, num in enumerate(end.split('.'))]) - sum([int(num) * (256 ** (3-i)) for i, num in enumerate(start.split('.'))])

print(ips_between("10.11.12.13", "10.11.13.0")) # 243
print(ips_between("20.0.0.10", "20.0.1.0"))     # 246
print(ips_between("10.0.0.0", "10.0.0.50"))     # 50