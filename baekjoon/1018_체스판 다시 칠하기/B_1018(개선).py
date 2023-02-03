def bw_check_w(dy, dx):
    # 첫번째를 흰색으로 칠할 때
    cnt = 0
    even_or_odd_y = dy % 2
    even_or_odd_x = dx % 2
    for k in range(dy, dy + 8):
        for l in range(dx, dx + 8):
            if cnt > min_cnt:
                return 2501
            # (dy 기준으로) 짝수번째 행
            if k % 2 == even_or_odd_y:
                # (dx 기준으로) 짝수번째 열
                if l % 2 == even_or_odd_x:
                    if arr[k][l] != "W":
                        cnt += 1
                # (dx 기준으로) 홀수번째 열
                else:
                    if arr[k][l] != "B":
                        cnt += 1
            # (dy 기준으로) 홀수번째 행
            else:
                # (dx 기준으로) 짝수번째 열
                if l % 2 == even_or_odd_x:
                    if arr[k][l] != "B":
                        cnt += 1
                # (dx 기준으로) 홀수번째 열
                else:
                    if arr[k][l] != "W":
                        cnt += 1
    return cnt


def bw_check_b(dy, dx):
    # 첫번째를 검정색으로 칠할 때
    cnt = 0
    even_or_odd_y = dy % 2
    even_or_odd_x = dx % 2
    for k in range(dy, dy + 8):
        for l in range(dx, dx + 8):
            if cnt > min_cnt:
                return 2501
            # (dy 기준으로) 짝수번째 행
            if k % 2 == even_or_odd_y:
                # (dx 기준으로) 짝수번째 열
                if l % 2 == even_or_odd_x:
                    if arr[k][l] != "B":
                        cnt += 1
                # (dx 기준으로) 홀수번째 열
                else:
                    if arr[k][l] != "W":
                        cnt += 1
            # (dy 기준으로) 홀수번째 행
            else:
                # (dx 기준으로) 짝수번째 열
                if l % 2 == even_or_odd_x:
                    if arr[k][l] != "W":
                        cnt += 1
                # (dx 기준으로) 홀수번째 열
                else:
                    if arr[k][l] != "B":
                        cnt += 1
    return cnt


N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
y = N - 8
x = M - 8
min_cnt = 2501
for i in range(y + 1):
    ay = i
    for j in range(x + 1):
        ax = j
        bw_cnt_b = bw_check_b(ay, ax)
        bw_cnt_w = bw_check_w(ay, ax)
        bw_cnt = min(bw_cnt_b, bw_cnt_w)
        if bw_cnt < min_cnt:
            min_cnt = bw_cnt
print(min_cnt)
