from collections import deque


def solution(n, t, m, time_table):
    def convert_to_minute(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)

    def convert_to_str(time):
        hour, minute = time // 60, time % 60
        return str(hour).zfill(2) + ":" + str(minute).zfill(2)

    def can_ride(time, crew):
        return time >= crew

    start = convert_to_minute("09:00")
    candidate = start
    time_table = deque(sorted(list(map(lambda x: convert_to_minute(x), time_table))))

    for _ in range(n):
        limit = m
        crews = []

        for _ in range(m):
            if time_table and can_ride(start, time_table[0]):
                limit -= 1
                crews.append(time_table.popleft())

        if not limit:
            candidate = crews[-1] - 1
        else:
            candidate = start
        start += t

    return convert_to_str(candidate)


# 참고
# 파이썬 알고리즘 인터뷰
