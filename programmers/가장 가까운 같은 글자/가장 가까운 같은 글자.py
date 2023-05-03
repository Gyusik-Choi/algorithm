def solution(s):
    answer = []

    # 뒤부터 탐색
    for i in range(len(s) - 1, 0, -1):
        back = s[i]
        is_find = False

        for j in range(i - 1, -1, -1):
            front = s[j]

            if back == front:
                is_find = True
                # 처음 발견한 같은 글자 간의 거리값 넣는다
                answer.append(i - j)
                break

        # 같은 글자를 못 찾은 경우 -1 넣는다
        if not is_find:
            answer.append(-1)

    # 첫번째 글자는 항상 -1
    answer.append(-1)
    return list(reversed(answer))

print(solution("banana"))
print(solution("foobar"))

