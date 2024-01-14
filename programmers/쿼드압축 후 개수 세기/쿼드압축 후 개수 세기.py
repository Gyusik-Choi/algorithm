# 4개로 분할
# n = len(arr)
# 길이가 // 2 씩 감소
# [y, y + n // 2, x, x + n // 2]
# [y, y + n // 2, x + n // 2, x + n]
# [y + n // 2, y + n, x, x + n // 2]
# [y + n // 2, y + n, x + n // 2, x + n]
def solution(arr):
    def is_all_same_number(lst):
        y_start, y_end, x_start, x_end = lst
        standard = arr[y_start][x_start]

        for i in range(y_start, y_end):
            for j in range(x_start, x_end):
                if standard != arr[i][j]:
                    return False

        return True

    def recursion(y, x, n, total_cnt):
        if n <= 1:
            return

        if not is_all_same_number([y, y + n // 2, x, x + n // 2]):
            recursion(y, x, n // 2, total_cnt)
        else:
            if arr[y][x] == 0:
                total_cnt[0] += 1
            else:
                total_cnt[1] += 1

        if not is_all_same_number([y, y + n // 2, x + n // 2, x + n]):
            recursion(y, x + n // 2, n // 2, total_cnt)
        else:
            if arr[y][x + n // 2] == 0:
                total_cnt[0] += 1
            else:
                total_cnt[1] += 1

        if not is_all_same_number([y + n // 2, y + n, x, x + n // 2]):
            recursion(y + n // 2, x, n // 2, total_cnt)
        else:
            if arr[y + n // 2][x] == 0:
                total_cnt[0] += 1
            else:
                total_cnt[1] += 1

        if not is_all_same_number([y + n // 2, y + n, x + n // 2, x + n]):
            recursion(y + n // 2, x + n // 2, n // 2, total_cnt)
        else:
            if arr[y + n // 2][x + n // 2] == 0:
                total_cnt[0] += 1
            else:
                total_cnt[1] += 1

        return total_cnt

    total_cnt = [0, 0]

    if len(arr[0]) == 1:
        if arr[0][0] == 0:
            total_cnt[0] += 0
        else:
            total_cnt[1] += 1
        return total_cnt

    if is_all_same_number([0, len(arr), 0, len(arr)]):
        if arr[0][0] == 0:
            total_cnt[0] += 1
        else:
            total_cnt[1] += 1
        return total_cnt

    return recursion(0, 0, len(arr), total_cnt)


print(solution([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]))
print(solution([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
]))
print(solution([[1]]))
print(solution([[1, 0], [1, 0]]))
print(solution([[1, 1], [1, 1]]))
