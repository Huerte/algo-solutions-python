from sqlalchemy.sql.base import elements


def rankTransformArray(n):
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    ranks = []