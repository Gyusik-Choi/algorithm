T = int(input())
for i in range(1, T + 1):
    N = int(input())
    x = N // 10
    y = N // 20
    cases = []
    for j in range(x + 1):
        for k in range(y + 1):
            if j + 2 * k == N // 10:
                cases.append([j, k])

    answer = 0
    for case in cases:
        if case[1] != 0:
            a = case[0] + case[1]
            b = case[1]

            sums_a = 1
            for m in range(1, a + 1):
                sums_a *= m

            sums_b = 1
            for n in range(1, b + 1):
                sums_b *= n

            sums_c = 1
            for o in range(1, a - b + 1):
                sums_c *= o

            answer += sums_a // (sums_b * sums_c) * (2 ** b)

        else:
            answer += 1

    print("#{} {}".format(i, answer))
