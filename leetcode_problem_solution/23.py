# better days

def betterDays(numberDays):
    days = []
    results = []

    for i in range(numberDays):
        days.append(int(input()))

    for i in range(len(days)):
        not_lucky = True
        for j in range(i + 1, len(days), 1):
            if days[i] < days[j]:
                results.append(j - i)
                not_lucky = False
                break
        if not_lucky:
            results.append(0)
    return results

print(betterDays(6))