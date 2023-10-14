def combine(n: int, k: int):
    def get_combinations(idx, number, temp, combs):
        if idx == k:
            combs.append(temp[:])
            return

        for num in range(number, n + 1):
            temp[idx] = num
            get_combinations(idx + 1, num + 1, temp, combs)

        return combs

    return get_combinations(0, 1, [0] * k, [])


print(combine(4, 2))
