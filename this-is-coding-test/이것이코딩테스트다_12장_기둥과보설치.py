def beam_possible(answer, x, y):
    # 기둥이 왼쪽 끝에 있는 경우
    if (x, y - 1, 0) in answer:
        return True

    # 기둥이 오른쪽 끝에 있는 경우
    if (x + 1, y - 1, 0) in answer:
        return True

    # 양쪽에 모두 보가 있는 경우
    if (x - 1, y, 1) in answer and (x + 1, y, 1) in answer:
        return True

    return False


def pillar_possible(answer, x, y):
    # 바닥에서 설치할 경우 가능
    if y == 0:
        return True

    # 아래에 기둥 있으면 가능
    if (x, y - 1, 0) in answer:
        return True

    # 보의 한 쪽 끝부분 위에 있으면 가능(보를 바닥에 설치하는 경우는 없음)
    # 왼쪽에 보가 있는 경우
    if (x - 1, y, 1) in answer:
        return True

    # 오른쪽에 보가 있는 경우
    if (x, y, 1) in answer:
        return True

    return False


def possible(answer):
    for x, y, knd in answer:
        if not knd:
            if pillar_possible(answer, x, y):
                continue
            else:
                return False
        else:
            if beam_possible(answer, x, y):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    answer = set()

    for frame in build_frame:
        x, y, knd, is_structuring = frame

        if not is_structuring:
            answer.remove((x, y, knd))
            if not possible(answer):
                answer.add((x, y, knd))
        else:
            answer.add((x, y, knd))
            if not possible(answer):
                answer.remove((x, y, knd))

    list_answer = []
    for a in answer:
        list_answer.append(list(a))

    list_answer.sort(key=lambda s: (s[0], s[1], s[2]))
    return list_answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

# 설치한 모든 요소들이 기준을 충족하는지 살펴봐야 한다
# 삭제해야 할때 해당하는 요소만 삭제하고 지을 수 없으면 다시 설치하려고 했으나
# (일단 이것부터 말이 안되긴 한다. 지을 수 있어서 지었던거라 애초에 항상 지웠다가 다시 지울 수 있다)
# 삭제했을때 그 주변에 있는 기둥이나 보가 기준을 충족하지 못할 수 있으므로 설치한 모든 요소들을 검사해야 한다

# 참고
# 이것이 코딩테스트다
# https://yjyoon-dev.github.io/kakao/2020/12/21/kakao-pillarfloor/
