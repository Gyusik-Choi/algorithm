def rotate(lst):
    rotated_lst = [[0] * len(lst) for _ in range(len(lst))]

    for i in range(len(lst)):
        for j in range(len(lst)):
            rotated_lst[j][len(lst) - 1 - i] = lst[i][j]

    return rotated_lst


arr = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(rotate(arr))
