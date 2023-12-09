def solution(elements):
    total_sums = set()
    length = len(elements)

    for i in range(length):
        sums = elements[i]
        total_sums.add(sums)

        for j in range(i + 1, i + length):
            sums += elements[j % length]
            total_sums.add(sums)

    return len(total_sums)


print(solution([7, 9, 1, 1, 4]))
