def is_beam_possible(history, x, y):
    # 기둥의 한쪽 끝 부분 위
    if [x, y - 1, 0] in history or [x + 1, y - 1, 0] in history:
        return True

    # 양쪽 끝 부분이 다른 보와 동시에 연결
    if [x - 1, y, 1] in history and [x + 1, y, 1] in history:
        return True

    return False


def is_pillar_possible(history, x, y):
    # 바닥 위
    if not y:
        return True

    # 보의 한쪽 끝 부분 위
    if [x - 1, y, 1] in history or [x, y, 1] in history:
        return True

    # 다른 기둥 위
    if [x, y - 1, 0] in history:
        return True

    return False


def is_possible(history):
    for idx, h in enumerate(history):
        x, y, a = h

        if not a:
            if not is_pillar_possible(history, x, y):
                return False
        else:
            if not is_beam_possible(history, x, y):
                return False

    # history 에 대한 for loop 를 모두 수행한 후에 True 를 반환 해야 한다
    # for loop 안에서 True 를 리턴 하면 history 를 다 검사할 수 없다
    return True


def solution(n, build_frame):
    build_history = []

    for idx, frame in enumerate(build_frame):
        x, y, a, b = frame

        if not b:
            build_history.remove([x, y, a])

            if not is_possible(build_history):
                build_history.append([x, y, a])
        else:
            build_history.append([x, y, a])

            if not is_possible(build_history):
                build_history.remove([x, y, a])

    return sorted(build_history, key=lambda c: (c[0], c[1], c[2]))


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
