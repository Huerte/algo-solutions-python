# Problem: Rank Records
# Source: 
# Note: Sorts records by descending score, then by name.


def rank_records(records):
    ranked = sorted(records, key=lambda record: (-record[1], record[0]))
    return [(position, name, score) for position, (name, score) in enumerate(ranked, start=1)]


if __name__ == "__main__":
    count = int(input())
    records = []

    for _ in range(count):
        name, score = input().split()
        records.append((name, int(score)))

    for position, name, score in rank_records(records):
        print(f"{position}. {name} - {score}")

    assert rank_records([("Bob", 90), ("Alice", 90), ("Cara", 85)]) == [
        (1, "Alice", 90),
        (2, "Bob", 90),
        (3, "Cara", 85),
    ]
