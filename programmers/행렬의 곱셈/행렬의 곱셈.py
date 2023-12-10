def solution(arr1, arr2):
    arr = []

    # y축
    # arr1 의 길이만큼 반복
    for i in range(len(arr1)):
        temp_arr = []

        # x축
        # arr2[0] 의 길이만큼 반복
        # arr2 는
        # y축 기준으로 x축 방향을 탐색하지 않고
        # x축 기준으로 y축 방향을 탐색해야 한다
        for j in range(len(arr2[0])):
            temp_sums = 0

            # arr1[0] 의 길이와 arr2 의 길이가 같아서
            # arr1 의 x축도 아래의 for 문으로 탐색 가능
            for k in range(len(arr2)):
                temp_sums += arr1[i][k] * arr2[k][j]
            temp_arr.append(temp_sums)

        arr.append(temp_arr)

    return arr


# print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
