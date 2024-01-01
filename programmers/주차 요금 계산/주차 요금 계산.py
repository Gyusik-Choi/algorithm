from collections import deque
import math


def solution(fees, records):
    def calculate_fee(record):
        time_sums = 0
        while len(record) >= 2:
            start = record.popleft()[0]
            end = record.popleft()[0]
            time_sums += calculate_time(start, end)

        # 들어 왔는데 나간 기록이 없는 경우
        if record:
            start = record.popleft()[0]
            time_sums += calculate_time(start, '')

        if fees[0] >= time_sums:
            return fees[1]
        return fees[1] + (math.ceil((time_sums - fees[0]) / fees[2]) * fees[3])

    def calculate_time(start, end):
        if not end:
            end = '23:59'
        end_hour, end_minute = list(map(lambda x: int(x), end.split(':')))
        start_hour, start_minute = list(map(lambda x: int(x), start.split(':')))
        return (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)

    history = dict()
    for r in records:
        time, number, state = r.split()
        if number in history:
            history[number].append([time, state])
        else:
            history[number] = deque([[time, state]])

    answer = []
    for h in sorted(history.keys()):
        answer.append(calculate_fee(history[h]))
    return answer


# 기본 시간, 기본 요금, 단위 시간, 단위 요금
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
