def solution(n, stages):
    stages_dict = {i: [] for i in range(1, n + 2)}
    for idx, stage in enumerate(stages):
        if not len(stages_dict[stage]):
            stages_dict[stage].append(1)
        else:
            stages_dict[stage][0] += 1

    total_number_of_people = len(stages)
    fail_rate = []
    for i in range(1, n + 1):
        fail_value = 0

        if len(stages_dict[i]):
            number_of_people = stages_dict[i][0]
            fail_value = number_of_people / total_number_of_people
            total_number_of_people -= number_of_people

        fail_rate.append([fail_value, i])

    fail_rate.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    for idx, fail in enumerate(fail_rate):
        answer.append(fail[1])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
