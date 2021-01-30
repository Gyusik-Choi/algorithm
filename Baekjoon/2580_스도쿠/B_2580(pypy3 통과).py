import sys


def back_track(cnt):
    if cnt == empty_arr_length:
        for item in arr:
            print(*item)
        sys.exit(0)

    m = empty_arr[cnt][0]
    n = empty_arr[cnt][1]

    possible_num = [0] + [1] * 9
    for o in range(9):
        if arr[m][o]:
            possible_num[arr[m][o]] = 0

        if arr[o][n]:
            possible_num[arr[o][n]] = 0

    am = m // 3 * 3
    an = n // 3 * 3
    for p in range(am, am + 3):
        for q in range(an, an + 3):
            num = arr[p][q]
            if num:
                possible_num[num] = 0

    possible_num_candidate = []
    for r in range(len(possible_num)):
        if possible_num[r] == 1:
            possible_num_candidate.append(r)

    # 시간초과 코드와의 차이는 여기서 발생한듯하다.
    # 시간초과 코드는 후보 숫자가 충족되지 않으면 다른 후보 숫자를 구하기 위한 연산을 처음부터 다시 해야하는데
    # 이 코드는 미리 후보 숫자들을 구해놓기 때문에 후보 숫자를 다시 연산할 필요가 없다.
    for candidate in possible_num_candidate:
        arr[m][n] = candidate
        back_track(cnt + 1)
        arr[m][n] = 0


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
empty_arr = [[i, j] for i in range(9) for j in range(9) if arr[i][j] == 0]
empty_arr_length = len(empty_arr)
back_track(0)
