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
        # 해당 영역의 숫자가 모두 동일한지 검사
        if is_all_same_number([y, y + n, x, x + n]):
            total_cnt[arr[y][x]] += 1
            return total_cnt

        # 4개 영역으로 분리
        recursion(y, x, n // 2, total_cnt)
        recursion(y + n // 2, x, n // 2, total_cnt)
        recursion(y, x + n // 2, n // 2, total_cnt)
        recursion(y + n // 2, x + n // 2, n // 2, total_cnt)
        return total_cnt

    return recursion(0, 0, len(arr), [0, 0])
