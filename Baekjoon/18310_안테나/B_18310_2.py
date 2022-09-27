def get_antenna_num():
    if len(houses) < 3:
        return houses[0]

    if not N % 2:
        return houses[N // 2 - 1]

    return houses[N // 2]


N = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(get_antenna_num())
