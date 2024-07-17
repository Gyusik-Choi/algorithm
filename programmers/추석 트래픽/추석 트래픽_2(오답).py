def solution(lines):
    def convert_to_second(time):
        time = time.split(':')
        return int(time[0]) * 3600000 + int(time[1]) * 60000 + int(time[2].split('.')[0]) * 1000 + int(time[2].split('.')[1])

    time_lines = []
    for line in lines:
        line = line.split(' ')
        start = convert_to_second(line[1])
        throughput = int(line[2][:-1].split('.')[0]) * 1000
        if len(line[2][:-1].split('.')) > 1:
            throughput += int(line[2][:-1].split('.')[1])
        time_lines.append([start, throughput])

    time_range = []
    for end, elapsed in time_lines:
        start = end + 1 - elapsed
        time_range.append([start, end])
    time_range = sorted(time_range)
    reversed_time_range = sorted(time_range)

    max_cnt = 0
    for idx, time in enumerate(time_range):
        start, end = time
        temp_cnt = 1
        for next_time in time_range[idx + 1:]:
            if start <= next_time[0] <= start + 999:
                temp_cnt += 1
        max_cnt = max(max_cnt, temp_cnt)

    for idx, time in enumerate(reversed_time_range):
        start, end = time
        temp_cnt = 1
        for next_time in time_range[idx + 1:]:
            if (next_time[0] <= end <= next_time[0] + 999) or (end <= next_time[0] <= end + 999):
                temp_cnt += 1
        max_cnt = max(max_cnt, temp_cnt)

    return max_cnt


print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
