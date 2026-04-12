# CodeWars - Human readable duration format

def format_duration(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    res = ""
    if y > 0:
        res += f"{y} year{'s' if y > 1 else ''}{', ' if any([s,d,h,m]) else ''}"
    if d > 0:
        res += f"{'and ' if all([a<0 for a in [h,m,s]]) and y > 0 else ''}{d} day{'s' if d > 1 else ''}{', ' if any([s,h,m]) else ''}"
    if h > 0:
        res += f"{'and ' if all([a<0 for a in [m,s]]) and any([d, y]) else ''}{h} hour{'s' if h > 1 else ''}"
        if m > 0:
            res += ', ' if s > 0 else ' and '
        elif s > 0:
            res += ' '
    if m > 0:
        res += f"{'and ' if s < 0 and any([y,d,h]) else ''}{m} minute{'s' if m > 1 else ''}{' ' if s > 0 else ''}"
    if s > 0:
        res += f"{'and ' if any([y,d,h,m]) else ''}{s} second{'s' if s > 1 else ''}"

    return res if res else 'now'

print(format_duration(62))         # 1 minute and 2 seconds
print(format_duration(31_556_926)) # 1 year and 1 second
print(format_duration(132030240))  #"4 years, 68 days, 3 hours and 4 minutes"