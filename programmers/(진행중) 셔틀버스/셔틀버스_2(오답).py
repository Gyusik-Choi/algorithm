# 탑승한 crew 는 제거해야 한다
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
    time_table = list(map(lambda x: convert_to_minute(x), time_table))
    time_table = deque(time_table)

    for i in range(n):
        limit = m
        crews = []

        j = 0
        length = len(time_table)
        while j < length:
            if not limit:
                break

            c = time_table.popleft()
            if can_ride(start, c):
                limit -= 1
                crews.append(c)
            else:
                time_table.append(c)

            j += 1

        crews.sort()

        # 다음 셔틀 X
        if i == n - 1:
            if not limit:
                return convert_to_str(crews[-1] - 1)
            return convert_to_str(start)

        start += t

    return convert_to_str(start)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(1, 1, 1, ["09:00"]))
print(solution(10, 60, 1, ["09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "18:00"]))
