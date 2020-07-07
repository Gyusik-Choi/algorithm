def crew_check(time_table, i, idx, m):
    # i는 셔틀버스 안에 시간, idx 는 타임 테이블의 인덱스, m은 최대 인원
    cnt = 0
    # idx 는 인덱스라 누적o, cnt 는 탑승인원이라 누적x
    # 인덱스가 time 배열의 길이보다 짧을 때 까지
    while idx < len(time_table):
        if i >= time_table[idx] and m >= cnt + 1:
            idx += 1
            cnt += 1
        else:
            break
    return [idx, cnt]
    # return 은 인덱스와 탑승 인원


def solution(n, t, m, timetable):
    shuttle = [540]
    for i in range(n - 1):
        shuttle.append(shuttle[-1] + t)

    crew_time = []
    for i in timetable:
        h = int(i[:2]) * 60
        mi = int(i[3:])
        crew_time.append(h + mi)
    time_table = sorted(crew_time)

    idx = [0]  # 인덱스
    last = []   # 마지막 버스 인원 체크(m이랑 비교), 총합은 몇 명이 버스에 탑승했는지 체크 가능.
    crews = m   # 최대 가능 승객
    for i in shuttle:
        num = crew_check(time_table, i, idx[-1], crews)
        idx.append(num[0])
        last.append(num[1])

    # 마지막 버스가 타 찼으면 마지막 탄 사람 보다 1분 빠르게
    # 여기가 핵심이다.
    # time_table 의 마지막 사람이 아니라 버스에 탄 마지막 사람 보다 1분 빨라야 한다.
    if last[-1] == m:
        ans_time = time_table[idx[-1] - 1] - 1
        hour = ans_time // 60
        minute = ans_time % 60
        ans_h = str(hour).zfill(2)
        ans_m = str(minute).zfill(2)
        print("{}:{}".format(ans_h, ans_m))
        return ans_h + ":" + ans_m

    # 마지막 버스 다 안찼으면 버스의 가장 마지막 시간
    else:
        ans_time = shuttle[-1]
        hour = ans_time // 60
        minute = ans_time % 60
        ans_h = str(hour).zfill(2)
        ans_m = str(minute).zfill(2)
        print("{}:{}".format(ans_h, ans_m))
        return ans_h + ":" + ans_m


solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
solution(2, 10, 2, ["09:10", "09:09", "08:00"])
solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(1, 1, 1, ["23:59"])
