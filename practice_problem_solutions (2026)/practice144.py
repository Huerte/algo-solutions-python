# CodeWars - The Solar System - Lost Moons

planet_moons = {
    'Mercury': [],
    'Venus': [],
    'Earth': ['Moon'],
    'Mars': ['Deimos', 'Phobos'],
    'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
    'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
    'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
    'Neptune': ['Nereid', 'Proteus', 'Triton']
}

def lost_moons(planets, moons):
    res = []
    for planet in sorted(planets, key=lambda x: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].index(x)):
        temp = [planet]
        right = True
        for moon in planet_moons[planet]:
            if moon in moons:
                if right:
                    temp.append(moon)
                else:
                    temp.insert(0, moon)
                right = not right
        res.append(temp)
    return res

print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Moon', 'Phobos', 'Europa'])) # [['Earth', 'Moon'], ['Mars', 'Phobos'], ['Jupiter', 'Europa']]
print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Deimos', 'Ganymede', 'Io'])) # [['Earth'], ['Mars', 'Deimos'], ['Jupiter', 'Ganymede', 'Io']]
print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Callisto', 'Dione', 'Iapetus'])) # [['Earth'], ['Mars'], ['Jupiter', 'Callisto']]