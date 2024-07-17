def solution(lines):
    def convert_time(time):
        hour, minute, second = time.split(":")
        sec, mil = second.split(".")
        return (int(hour) * 60 * 60 * 1000) + (int(minute) * 60 * 1000) + (int(sec) * 1000) + int(mil)

    def convert_second(second):
        sec = second[:-1].split(".")
        if len(sec) > 1:
            return (int(sec[0]) * 1000) + int(sec[1])
        return int(sec[0]) * 1000

    def calculate_start_time(end_time, duration):
        return convert_time(end_time) - convert_second(duration) + 1

    lines_without_date = [line.split()[1:] for line in lines]
    times = [[calculate_start_time(line[0], line[1]), convert_time(line[0])] for line in lines_without_date]

    max_throughput = 1
    for i in range(len(times)):
        temp = 1
        end = times[i][1] + 1000
        for j in range(i + 1, len(times)):
            start = times[j][0]
            if end > start:
                temp += 1
        max_throughput = max(max_throughput, temp)
    return max_throughput


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))
# print(solution([
#     "2016-09-15 01:00:04.002 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))
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
