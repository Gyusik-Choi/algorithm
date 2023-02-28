def solution(number):
    def get_combinations(cnt, cnt_limit, num, num_limit, combination):
        if cnt == cnt_limit:
            combinations.append(combination[:])
            return

        for n in range(num, num_limit):
            combination.append(number[n])
            get_combinations(cnt + 1, cnt_limit, n + 1, num_limit, combination)
            combination.pop()


    combinations = []
    get_combinations(0, 3, 0, len(number), [])

    answer = 0

    for idx, comb in enumerate(combinations):
        if sum(comb) == 0:
            answer += 1

    return answer


print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))
