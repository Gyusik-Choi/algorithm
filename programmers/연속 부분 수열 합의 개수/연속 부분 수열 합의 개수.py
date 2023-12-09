def solution(elements):
    total_sums = set()
    length = len(elements)

    for long in range(1, length):
        for j in range(length):
            sums = 0
            sums += sum(elements[j: j + long])
            if j + long >= length:
                sums += sum(elements[:(j + long) % length])
            total_sums.add(sums)

    total_sums.add(sum(elements))
    return len(total_sums)


print(solution([7, 9, 1, 1, 4]))
