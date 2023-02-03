def sliding_window():
    start = 0
    end = 0
    limit = len(prime_numbers)
    sums = prime_numbers[start]

    answer = 0
    while start <= end < limit:
        if sums >= N:
            if sums == N:
                answer += 1
            sums -= prime_numbers[start]
            start += 1
        else:
            if end + 1 < limit:
                end += 1
                sums += prime_numbers[end]
            else:
                break

    return answer


N = int(input())
if N == 1:
    print(0)
else:
    numbers = [1] * (N + 1)

    n = 2
    while n <= N:
        if numbers[n]:
            x = n * 2
            while x <= N:
                numbers[x] = 0
                x += n
        n += 1

    prime_numbers = []
    for i in range(2, N + 1):
        if numbers[i] == 1:
            prime_numbers.append(i)

    print(sliding_window())

# https://wikidocs.net/21638
# https://www.acmicpc.net/board/view/73979
