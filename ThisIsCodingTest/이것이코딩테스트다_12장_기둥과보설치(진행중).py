# ?? 같은 점에 보와 기둥이 동시에 올 수도 있는데 이는 어떻게 ?? (한 점에서 위로 기둥, 오른쪽 보)
# => 기둥과 보를 따로 설치 여부를 판단 하거나 해야함
# 간과한 점은
# 삭제해야할때 일단 삭제하고 지을 수 없으면 다시 설치하려고 했으나
# (일단 이것부터 말이 안되긴 한다. 지을 수 있어서 지어져 있던거라 애초에 항상 지웠다가 다시 지울 수 있다)
# 이러면 해당하는 부분만 보게 되는데 삭제했을때 그 주변에 있는 기둥이나 보가 기준을 충족하지 못할 수 있으므로
# 설치한 모든 요소들이 기준을 충족하는지 살펴봐야 한다


def destructuring(wall, y, x, knd):
    if not knd:
        wall[y][x][0] = -1
    else:
        wall[y][x][1] = -1


def structuring(wall, y, x, knd):
    if not knd:
        wall[y][x][0] = 0
    else:
        wall[y][x][1] = 1


def beam_possible(wall, y, x):
    # 기둥이 왼쪽 끝에 있는 경우
    if wall[y - 1][x][0] == 0:
        return True

    # 기둥이 오른쪽 끝에 있는 경우
    if wall[y - 1][x + 1][0] == 0:
        return True

    # 양쪽에 모두 보가 있는 경우
    if wall[y][x - 1][1] == 1 and wall[y][x + 1][1] == 1:
        return True

    return False


def pillar_possible(wall, y, x):
    # 바닥에서 설치할 경우 가능
    if y == 0:
        return True

    # 아래에 기둥 있으면 가능
    if wall[y - 1][x][0] == 0:
        return True

    # 보의 한 쪽 끝부분 위에 있으면 가능(보를 바닥에 설치하는 경우는 없음)
    # 왼쪽에 보가 있는 경우
    if wall[y][x - 1][1] == 1:
        return True

    # 오른쪽에 보가 있는 경우
    if wall[y][x][1] == 1:
        return True

    return False


def possible(wall, answer):
    for x, y, knd, is_structuring in answer:
        if not knd:
            if pillar_possible(wall, y, x):
                continue
            else:
                return False
        else:
            if beam_possible(wall, y, x):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    # 기둥, 보
    # 한 점에 둘 다 오는 경우를 대비해 인덱스 따로 둠 (3차원 배열)
    answer = []
    wall = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]

    for frame in build_frame:
        x, y, knd, is_structuring = frame

        if not is_structuring:
            if [x, y, knd, 1] in answer:
                answer.remove([x, y, knd, is_structuring])
                destructuring(wall, y, x, knd)
            if not possible(wall, answer):
                answer.append([x, y, knd, is_structuring])
                structuring(wall, y, x, knd)
        else:
            answer.append([x, y, knd, is_structuring])
            structuring(wall, y, x, knd)
            if not possible(wall, answer):
                answer.remove([x, y, knd, is_structuring])
                destructuring(wall, y, x, knd)

    answer.sort(key=lambda a: a[0])
    return answer


# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
