def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    if len(data) < 1:
        return []

    result = []
    filtered = sorted([x.get("price", 0) for x in data])[limit * -1:]
    for i in range(len(filtered)):
        for dic in data:
            if dic.get("price") == filtered[i]:
                result.append(dic)
                break
    return result


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
