# time_table 이 정렬되어 있지 않다
# crews 에서 가장 늦게 탄 인원을 찾아야 할 경우에 정렬이 필요한데
# 이를 편리하게 하기 위해 time_table 을 분으로 변환해서 계산
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

    for i in range(n):
        limit = m
        crews = []

        for c in time_table:
            if not limit:
                break
            if can_ride(start, c):
                limit -= 1
                crews.append(c)

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
