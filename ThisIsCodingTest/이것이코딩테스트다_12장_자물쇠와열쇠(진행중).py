import copy


def compare(key_items, lock_items):
    for i in range(len(key_items)):
        if key_items[i] == 1 and lock_items[i] == 1:
            return False

    return True


def is_fit(key, lock):
    # 깊은 복사 후 180도 회전
    new_key = copy.deepcopy(key)
    for _ in range(2):
        rotated_key = rotate(new_key)
        new_key = rotated_key

    # 왼쪽 상단
    key_items_upper_left = []
    lock_items_upper_left = []

    for i in range(len(new_key)):
        for j in range(len(new_key)):
            key_items_upper_left.append(new_key[i][j])
            lock_items_upper_left.append(lock[i][j])

            compare_result = compare(key_items_upper_left, lock_items_upper_left)

            if compare_result:
                return True

    # 오른쪽 상단
    key_items_upper_right = []
    lock_items_upper_right = []

    for i in range(len(new_key) - 1, -1, -1):
        for j in range(len(new_key) - 1, -1, -1):
            key_items_upper_right.append(new_key[i][j])
            lock_items_upper_right.append(lock[i][j])

            compare_result = compare(key_items_upper_right, lock_items_upper_right)

            if compare_result:
                return True

    # 왼쪽 하단 늘어나는 부분
    # i는 감소
    # j는 증가
    key_items_lower_left = []
    lock_items_lower_left = []

    for i in range(len(new_key) - 1, -1, -1):
        for j in range(len(new_key)):
            key_items_lower_left.append(new_key[i][j])
            lock_items_lower_left.append(lock[i][j])

            compare_result = compare(key_items_lower_left, lock_items_lower_left)

            if compare_result:
                return True

    # 오른쪽 하단
    key_items_lower_right = []
    lock_items_lower_right = []

    for i in range(len(new_key) - 1, -1, -1):
        for j in range(len(new_key)):
            key_items_lower_right.append(new_key[i][j])
            lock_items_lower_right.append(lock[i][j])

            compare_result = compare(key_items_lower_right, lock_items_lower_right)

            if compare_result:
                return True

    return False


def rotate(key):
    # 90도 회전
    rotated_key = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            rotated_key[j][len(key) - 1 - i] = key[i][j]

    return rotated_key


def solution(key, lock):
    new_key = copy.deepcopy(key)
    for _ in range(4):
        rotated_key = rotate(new_key)
        new_key = rotated_key

        is_fit_result = is_fit(new_key, lock)

        if is_fit_result:
            return True
        return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [1, 0, 0]], [[1, 1, 0], [1, 1, 1], [1, 1, 1]]))

# 완전탐색
# 4방향 돌려줘야 한다
# 자물쇠의 홈에 맞춰야 한다

# true, false 만 찾으면 되니까 하나라도 충족하면 더 이상 탐색 안 해도 된다

# 비교를 위해서는 key 를 180 도 회전해야 한다
