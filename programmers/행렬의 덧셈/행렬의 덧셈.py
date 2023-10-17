def solution(arr1, arr2):
    y = len(arr1)
    x = len(arr1[0])

    arr3 = [[0] * x for _ in range(y)]

    for i in range(y):
        for j in range(x):
            arr3[i][j] = arr1[i][j] + arr2[i][j]

    return arr3


print(solution([[1, 2], [2, 3]],[[3, 4], [5, 6]]))
