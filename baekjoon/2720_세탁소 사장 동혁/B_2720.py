T = int(input())
for _ in range(T):
    C = int(input())

    changes = [25, 10, 5, 1]
    answer = []

    for change in changes:
        quotient, remainder = divmod(C, change)

        C = remainder
        answer.append(quotient)

    print(*answer)

