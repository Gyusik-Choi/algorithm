def solution(n, arr1, arr2):
    arr_bin = list(bin(a | b) for a, b in zip(arr1, arr2))
    return [bi[2:].zfill(n).replace('0', ' ').replace('1', '#') for bi in arr_bin]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
