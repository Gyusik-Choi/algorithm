def is_pillar_possible(build_history, x, y):
    if not y:
        return True

    if [x, y - 1, 0] in build_history:
        return True

    if [x - 1, y, 1] in build_history:
        return True

    if [x, y, 1] in build_history:
        return True

    return False


def is_beam_possible(build_history, x, y):
    if [x, y - 1, 0] in build_history:
        return True

    if [x + 1, y - 1, 0] in build_history:
        return True

    if [x - 1, y, 1] in build_history and [x + 1, y, 1] in build_history:
        return True

    return False


def is_possible(build_history):
    for idx, history in enumerate(build_history):
        x, y, is_beam = history

        if is_beam and not is_beam_possible(build_history, x, y):
            return False

        if not is_beam and not is_pillar_possible(build_history, x, y):
            return False

    return True


def solution(n, build_frame):
    wall = [[-1] * (n + 1) for _ in range(n + 1)]

    build_history = []

    for idx, frame in enumerate(build_frame):
        x, y, is_beam, is_install = frame

        if is_install:
            build_history.append(frame[:3])

            if not is_possible(build_history):
                build_history.remove(frame[:3])
        else:
            build_history.remove(frame[:3])

            if not is_possible(build_history):
                build_history.append(frame[:3])

    return sorted(build_history, key=lambda a: (a[0], a[1], a[2]))


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

