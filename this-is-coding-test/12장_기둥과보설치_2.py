def check_per_element(value, answer):
    x, y, a = value

    # 기둥
    if not a:
        if y == 0:
            return True

        if [x, y - 1, 0] in answer:
            return True

        if [x - 1, y, 1] in answer:
            return True

        if [x, y, 1] in answer:
            return True

        return False
    # 보
    else:
        if [x, y - 1, 0] in answer:
            return True

        if [x + 1, y - 1, 0] in answer:
            return True

        if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            return True

        return False


def is_possible(answer):
    # False 가 나오는 경우가 없어야 조건을 만족함
    for idx, value in enumerate(answer):
        if not check_per_element(value, answer):
            return False

    return True


def solution(n, build_frame):
    answer = []

    for idx, frame in enumerate(build_frame):
        # x축, y축, 기둥 or 보, 삭제 or 설치
        x, y, a, is_build = frame

        if not is_build:
            # 이전에 설치 했던 것을 삭제 할 수 있는데
            # pop() 을 하게 되면 바로 이전의 설치 한 것만 삭제 할 수 있음
            # 삭제 대상을 정확히 찾기 위해 remove 를 사용함
            answer.remove([x, y, a])
            if not is_possible(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not is_possible(answer):
                answer.remove([x, y, a])

    # sort 는 리턴 하는게 없어서
    # return answer.sort(key=lambda z: (z[0], z[1], z[2]))
    # 이렇게 하면 None 을 리턴 하므로 주의
    answer.sort(key=lambda z: (z[0], z[1], z[2]))
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# => [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
# => [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
