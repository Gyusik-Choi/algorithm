def is_lock_empty(lock_table, lock_y, lock_x, lock_length):
    for i in range(lock_length):
        for j in range(lock_length):
            if lock_table[lock_y + i][lock_x + j] != 1:
                return False

    return True


def is_key_in_lock(lock_table, y, x):
    return lock_table[y][x] != -1


def compare(key_table, lock_table, key_y, key_x, lock_y, lock_x, key_length, lock_length):
    for i in range(key_length):
        for j in range(key_length):
            y = key_y + i
            x = key_x + j

            if is_key_in_lock(lock_table, y, x):
                if key_table[y][x] == 1 and lock_table[y][x] == 1:
                    return False

                if key_table[y][x] == 1 and lock_table[y][x] == 0 or key_table[y][x] == 0 and lock_table[y][x] == 1:
                    lock_table[y][x] = 1

    if is_lock_empty(lock_table, lock_y, lock_x, lock_length):
        return True

    return False


def set_plus_key_table(key_table, key, y, x):
    for i in range(len(key)):
        for j in range(len(key)):
            key_table[y + i][x + j] = key[i][j]


def set_minus_key_table(key_table, key, y, x):
    for i in range(len(key)):
        for j in range(len(key)):
            key_table[y + i][x + j] = 0


def set_lock_table(lock_table, lock, key_length):
    for i in range(len(lock)):
        for j in range(len(lock)):
            lock_table[i + key_length - 1][j + key_length - 1] = lock[i][j]


def compare_key_and_lock_table(key_table, lock_table, key, lock):
    lock_y = len(key) - 1
    lock_x = len(key) - 1

    for i in range(len(key_table) - len(key) + 1):
        for j in range(len(key_table) - len(key) + 1):
            set_plus_key_table(key_table, key, i, j)
            set_lock_table(lock_table, lock, len(key))

            if compare(key_table, lock_table, i, j, lock_y, lock_x, len(key), len(lock)):
                return True

            set_minus_key_table(key_table, key, i, j)

    return False


def rotate_key(key):
    new_key = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(new_key)):
        for j in range(len(new_key)):
            new_key[j][len(key) - i - 1] = key[i][j]

    return new_key


# 열쇠 돌기 (1), 자물쇠 홈 (0)
def solution(key, lock):
    m = len(key)
    n = len(lock)

    key_table = [[0] * (n + (m - 1) * 2) for _ in range(n + (m - 1) * 2)]
    lock_table = [[-1] * (n + (m - 1) * 2) for _ in range(n + (m - 1) * 2)]

    for i in range(4):
        rotated_key = rotate_key(key)
        key = rotated_key

        if compare_key_and_lock_table(key_table, lock_table, rotated_key, lock):
            return True

    return False


# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
# => True
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1]]))
# => True
print(solution([[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]))
