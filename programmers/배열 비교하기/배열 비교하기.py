def solution(arr1, arr2):
    n, m = len(arr1), len(arr2)
    n_sum, m_sum = sum(arr1), sum(arr2)

    if n != m:
        return 1 if n > m else -1
    return 0 if n_sum == m_sum else 1 if n_sum > m_sum else -1


print(solution([49, 13], [70, 11, 2]))
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))
