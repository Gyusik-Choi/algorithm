def combine(n: int, k: int):
    def get_combinations(cnt, number, temp, combs):
        if cnt == k:
            combs.append(temp[:])
            return

        for num in range(number, n + 1):
            temp.append(num)
            get_combinations(cnt + 1, num + 1, temp, combs)
            temp.pop()

        return combs

    return get_combinations(0, 1, [], [])


print(combine(4, 2))
