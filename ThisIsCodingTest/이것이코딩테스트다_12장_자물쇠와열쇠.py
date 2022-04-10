import copy


def minus(key_and_lock, key, key_length, y, x):
    for i in range(key_length):
        for j in range(key_length):
            key_and_lock[i + y][j + x] -= key[i][j]


def plus(key_and_lock, key, key_length, y, x):
    for i in range(key_length):
        for j in range(key_length):
            key_and_lock[i + y][j + x] += key[i][j]


def fit_check(key_and_lock, key_length, lock_length):
    # 자물쇠 길이만큼 체크
    # 체크하는 위치에 주의
    # 더해진 곳을 체크하는게 아니라 중앙에 있는 자물쇠를 체크해야 한다
    for i in range(lock_length):
        for j in range(lock_length):
            if key_and_lock[key_length + i][key_length + j] != 1:
                return False

    return True


def is_fit(key_and_lock, key, key_length, lock_length, y, x):
    plus(key_and_lock, key, key_length, y, x)

    fit_result = fit_check(key_and_lock, key_length, lock_length)

    minus(key_and_lock, key, key_length, y, x)

    if fit_result:
        return True

    return False


def rotate(key):
    rotated_key = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            rotated_key[j][len(key) - 1 - i] = key[i][j]

    return rotated_key


def put_lock_center(key_and_lock, lock, lock_length, key_length):
    for i in range(key_length, key_length + lock_length):
        for j in range(key_length, key_length + lock_length):
            key_and_lock[i][j] = lock[i - key_length][j - key_length]


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)

    key_and_lock = [[0] * (key_length * 2 + lock_length) for _ in range(key_length * 2 + lock_length)]

    put_lock_center(key_and_lock, lock, lock_length, key_length)

    new_key = copy.deepcopy(key)
    for _ in range(4):
        rotated_key = rotate(new_key)
        new_key = rotated_key

        for i in range(1, key_length + lock_length):
            for j in range(1, key_length + lock_length):
                if is_fit(key_and_lock, new_key, key_length, lock_length, i, j):
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 참고
# 이것이 코딩테스트다
# https://velog.io/@tjdud0123/자물쇠와-열쇠-2020-카카오-공채-python
