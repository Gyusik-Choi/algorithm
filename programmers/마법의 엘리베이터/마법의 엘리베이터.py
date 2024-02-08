def solution(storey):
    def get_min_move(floor, cnt):
        if floor == 0:
            return cnt

        cur = floor % 10
        floor //= 10
        if cur > 5:
            return get_min_move(floor + 1, cnt + (10 - cur))
        elif cur < 5:
            return get_min_move(floor, cnt + cur)
        else:
            next = floor % 10
            if next >= 5:
                return get_min_move(floor + 1, cnt + (10 - cur))
            return get_min_move(floor, cnt + cur)

    return get_min_move(storey, 0)


# 반례
# https://school.programmers.co.kr/questions/41779
print(solution(545))
