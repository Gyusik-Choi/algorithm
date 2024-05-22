import copy


def rotate_key(key):
    rotated_door = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            rotated_door[j][len(key) - i - 1] = key[i][j]
    
    return rotated_door


def is_unlocked(door, key, lock):
    n = len(lock)
    m = len(key)

    for i in range(n + m - 1):
        for j in range(n + m - 1):
            if door[i][j] == 0 or door[i][j] == 2:
                return False
    
    return True


def put_key_on_door(door, key, lock, y, x):
    n = len(lock)
    m = len(key)

    for i in range(m):
        for j in range(m):
            if door[y + i][x + j] == -1:
                continue

            door[y + i][x + j] += key[i][j]


def put_lock_on_door(door, key, lock):
    n = len(lock)
    m = len(key)

    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            door[i][j] = lock[i + 1 - m][j + 1 - m]


def solution(key, lock):
    # 자물쇠 1, 열쇠 1 (X)
    # 자물쇠 1, 열쇠 0 (O)
    # 자물쇠 0, 열쇠 0 (X)
    # 자물쇠 0, 열쇠 1 (O)

    # door 가운데 자물쇠 놓는다
    # 3차 for loop 를 돌아야 한다
    # 키를 90도씩 회전시켜 4번을 1차 for loop 돌면서
    # n + m - 1 만큼 2차 for loop 돌면서 열쇠를 놓는다
    # 이를 key 를 4번 수행해야 한다
    # 자물쇠 열쇠 값 더해서 1이면 괜찮다
    # 그러나 0이나 2면 안 된다

    # 겹치는 부분 체크는 어떻게?
    # -> 자물쇠와 겹치는 열쇠가 아니면 배열에 놓지 않는다
    # -> 배열에서 자물쇠는 0, 1로 되어있고 나머지는 -1로 되어 있다
    # -> -1인 부분은 무시하고 0, 1인 부분만 더한 뒤에
    # -> 배열 전체 돌면서 0 혹은 2가 있는지 체크
    # -> 0 혹은 2가 하나도 없으면 true 리턴

    # 배열 복사는 얼마나?
    # -> 자물쇠 놓은 배열을 열쇠를 하나 놓을 때 마다 복사한다

    n = len(lock)
    m = len(key)

    door_length = n + (m - 1) * 2
    door = [[-1] * door_length for _ in range(door_length)]

    put_lock_on_door(door, key, lock)

    for k in range(4):
        key = rotate_key(key)

        for i in range(n + m - 1):
            for j in range(n + m - 1):
                copied_door = copy.deepcopy(door)

                put_key_on_door(copied_door, key, lock, i, j)

                if is_unlocked(copied_door, key, lock):
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# True
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]))
# True
print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]))
# True
print(solution([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# False