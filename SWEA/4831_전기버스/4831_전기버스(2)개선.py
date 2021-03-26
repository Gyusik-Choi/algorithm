T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = [i for i in range(N + 1)]
    stations = list(map(int, input().split()))

    charges = 0
    location = 0
    while location + K < N:
        for i in range(location + K, location, -1):
            if stops[i] in stations:
                location = i
                charges += 1
                break
        else:
            charges = 0
            break
    print("#{} {}".format(t, charges))
