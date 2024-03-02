def solution(data, col, row_begin, row_end):
    def sort_data(arr):
        return sorted(arr, key=lambda x: (x[col - 1], -x[0]))

    def get_sums(arr, start, end):
        sums_lst = []
        for i in range(start - 1, end):
            temp_sum = 0
            for j in range(len(arr[i])):
                temp_sum += arr[i][j] % (i + 1)
            sums_lst.append(temp_sum)
        return sums_lst

    def get_hash_value(arr):
        hash_value = arr[0]
        for i in range(1, len(arr)):
            hash_value ^= arr[i]
        return hash_value

    data = sort_data(data)
    sums = get_sums(data, row_begin, row_end)
    return get_hash_value(sums)


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))

