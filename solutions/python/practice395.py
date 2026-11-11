# Problem: Cookies
# Source: https://py.checkio.org/
# Note: Parses and retrieves cookie value by name
def get_cookie(cookie, name):
    cont = [word.strip() for word in cookie.split(';')]
    
    for prt in cont:
        key, val = prt.split('=', 1)
        if key == name:
            return val

print(get_cookie("theme=light; sessionToken=abc123", "sessionToken")) # "abc123"
print(get_cookie("theme=light; sessionToken=abc123", "userId"))       # None
print(get_cookie("theme=light; sessionToken=abc123", "theme"))        # "light"
