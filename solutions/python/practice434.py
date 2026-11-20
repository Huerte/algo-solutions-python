# Problem: Sun Angle
# Source: https://py.checkio.org/en/mission/sun-angle/
# Topic: Math, String

def sun_angle(time):
    h, m = map(int, time.split(":"))
    total_minutes = h * 60 + m

    start = 6 * 60
    end = 18 * 60

    if total_minutes < start or total_minutes > end:
        return "I don't see the sun!"

    # 720 minutes from sunrise to sunset -> 180 / 720 = 0.25 deg per min
    angle = (total_minutes - start) * 0.25
    return round(angle, 2)

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75
assert sun_angle("01:23") == "I don't see the sun!"
assert sun_angle("18:00") == 180
assert sun_angle("06:00") == 0
