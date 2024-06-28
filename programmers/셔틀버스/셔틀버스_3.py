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
    time_table = sorted(list(map(lambda x: convert_to_minute(x), time_table)))

    for _ in range(n):
        limit = m
        crews = []

        for _ in range(m):
            if time_table and can_ride(start, time_table[0]):
                limit -= 1
                crews.append(time_table.pop(0))

        if not limit:
            candidate = crews[-1] - 1
        else:
            candidate = start
        start += t

    return convert_to_str(candidate)


# 셔틀버스_2.py 와 차이는
# deque 의 사용 유무다
# 이 풀이는 deque 가 아닌 리스트를 활용했다
# 시간 차이는 그리 나지 않았다
#
# deque 사용 했을 경우 프로그래머스 시간
# 테스트 1 〉	    통과 (0.03ms, 10.4MB)
# 테스트 2 〉   	통과 (0.03ms, 10.4MB)
# 테스트 3 〉   	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	    통과 (0.04ms, 10.4MB)
# 테스트 5 〉	    통과 (0.04ms, 10.5MB)
# 테스트 6 〉   	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	    통과 (0.39ms, 10.5MB)
# 테스트 8 〉	    통과 (0.02ms, 10.4MB)
# 테스트 9 〉	    통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.4MB)
# 테스트 11 〉	통과 (0.08ms, 10.3MB)
# 테스트 12 〉	통과 (0.36ms, 10.4MB)
# 테스트 13 〉	통과 (0.36ms, 10.4MB)
# 테스트 14 〉	통과 (0.20ms, 10.3MB)
# 테스트 15 〉	통과 (0.14ms, 10.4MB)
# 테스트 16 〉	통과 (0.37ms, 10.3MB)
# 테스트 17 〉	통과 (0.58ms, 10.4MB)
# 테스트 18 〉	통과 (0.68ms, 10.3MB)
# 테스트 19 〉	통과 (0.34ms, 10.4MB)
# 테스트 20 〉	통과 (0.68ms, 10.5MB)
# 테스트 21 〉	통과 (1.04ms, 10.6MB)
# 테스트 22 〉	통과 (0.40ms, 10.3MB)
# 테스트 23 〉	통과 (0.36ms, 10.4MB)
# 테스트 24 〉	통과 (1.03ms, 10.6MB)
#
# 리스트 사용 했을 경우 프로그래머스 시간
# 테스트 1 〉   	통과 (0.04ms, 10.3MB)
# 테스트 2 〉   	통과 (0.03ms, 10.3MB)
# 테스트 3 〉   	통과 (0.04ms, 10.4MB)
# 테스트 4 〉   	통과 (0.04ms, 10.4MB)
# 테스트 5 〉   	통과 (0.05ms, 10.3MB)
# 테스트 6 〉   	통과 (0.03ms, 10.5MB)
# 테스트 7 〉	    통과 (0.49ms, 10.4MB)
# 테스트 8 〉	    통과 (0.03ms, 10.3MB)
# 테스트 9 〉	    통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.5MB)
# 테스트 11 〉	통과 (0.08ms, 10.4MB)
# 테스트 12 〉	통과 (0.38ms, 10.4MB)
# 테스트 13 〉	통과 (0.37ms, 10.4MB)
# 테스트 14 〉	통과 (0.10ms, 10.5MB)
# 테스트 15 〉	통과 (0.14ms, 10.4MB)
# 테스트 16 〉	통과 (0.20ms, 10.3MB)
# 테스트 17 〉	통과 (0.38ms, 10.4MB)
# 테스트 18 〉	통과 (0.35ms, 10.5MB)
# 테스트 19 〉	통과 (0.38ms, 10.4MB)
# 테스트 20 〉	통과 (0.63ms, 10.5MB)
# 테스트 21 〉	통과 (1.15ms, 10.5MB)
# 테스트 22 〉	통과 (0.67ms, 10.5MB)
# 테스트 23 〉	통과 (0.35ms, 10.4MB)
# 테스트 24 〉	통과 (1.12ms, 10.4MB)