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
    # time_table 을 정렬해야 한다
    # 기존에는 crews.sort() 를 아래에서 수행 했는데
    # time_table 을 정렬 하면서 crews 를 정렬할 필요가 없어져서 주석처리
    # time_table 이 정렬되지 않으면 더 앞선 시간에 줄을 선 크루가
    # crews 에 들어오지 못하는 경우가 생길 수 있어서 crews 를 정렬 하더라도 오답이 나올 수 있다
    # 반례 -> 1, 10, 3, ["08:59", "08:58", "08:57", "08:56", "08:55"]
    time_table = deque(sorted(list(map(lambda x: convert_to_minute(x), time_table))))

    for i in range(n):
        limit = m
        # 탑승한 crew 는 time_table 에서 제거해야 한다
        crews = []

        j = 0
        length = len(time_table)
        while j < length:
            if not limit:
                break
            j += 1
            c = time_table.popleft()
            if can_ride(start, c):
                limit -= 1
                crews.append(c)
            else:
                time_table.append(c)

        # time_table 을 정렬하면
        # 앞선 시간 순으로 crews 에 들어오기 때문에
        # crews 를 정렬할 필요가 없다
        # crews.sort()

        # 다음 셔틀 X
        if i == n - 1:
            if not limit:
                return convert_to_str(crews[-1] - 1)
            return convert_to_str(start)

        start += t


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
# print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
# print(solution(1, 1, 1, ["23:59"]))
# print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
# print(solution(1, 1, 1, ["09:00"]))
# print(solution(10, 60, 1, ["09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "09:00", "18:00"]))
# print(solution(2, 10, 3, ["09:05", "09:09", "09:13"]))
# print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01", "00:02", "00:03", "00:04"]))
# print(solution(1, 10, 3, ["08:55", "08:55", "08:59"]))
# print(solution(1, 10, 3, ["08:59", "08:58", "08:57", "08:56", "08:55"]))

# 참고
# https://school.programmers.co.kr/questions/3571
