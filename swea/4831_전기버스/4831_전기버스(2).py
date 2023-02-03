T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = [i for i in range(N + 1)]
    stations = list(map(int, input().split()))

    charges = 0

    flag_location = 0
    location = 0

    while location < N:
        location += K
        if location >= N:
            break

        check = False
        for i in range(location, flag_location, -1):
            if stops[i] in stations:
                location = i
                flag_location = i
                charges += 1
                check = True
                break

        if not check:
            charges = 0
            break
    print("#{} {}".format(t, charges))
