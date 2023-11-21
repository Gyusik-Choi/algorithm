def get_answer_cnt(answers, pattern):
    cnt = 0
    length = len(pattern)
    for idx, answer in enumerate(answers):
        i = idx % length
        if answer == pattern[i]:
            cnt += 1
    return cnt


def solution(answers):
    first_cnt = get_answer_cnt(answers, [1, 2, 3, 4, 5])
    second_cnt = get_answer_cnt(answers, [2, 1, 2, 3, 2, 4, 2, 5])
    third_cnt = get_answer_cnt(answers, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    counts = [first_cnt, second_cnt, third_cnt]
    max_cnt = max(counts)

    answer = []
    for idx, cnt in enumerate(counts):
        if cnt == max_cnt:
            answer.append(idx + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
