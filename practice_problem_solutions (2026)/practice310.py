# py.checkio - The Highest Building

def highest_building(buildings: list[list[int]]) -> list[int]:
    
    cur_max = float('-inf')
    ind = -1

    n = len(buildings) - 1
    for col in range(len(buildings[0])):
        row = n
        
        while row >= 0 and buildings[row][col] == 1:
            row -= 1
        
        new_height = n - row
        if new_height > cur_max:
            ind = col
            cur_max = new_height

    return [ind + 1, cur_max]


print(highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])) # [4, 1]
print(highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]])) # [3, 4]
print(highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])) # [3, 2]