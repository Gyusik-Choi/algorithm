def solution(n, arr1, arr2):
    arr_bin = list(bin(a | b) for a, b in zip(arr1, arr2))
    arr_bin = [binary[2:].zfill(n) for binary in arr_bin]
    return [''.join(map(lambda x: '#' if x == '1' else ' ', binary)) for binary in arr_bin]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
