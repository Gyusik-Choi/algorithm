def set_lock(grid, key, lock):
    m = len(key)
    n = len(lock)
    lock_start = m - 1

    for i in range(lock_start, lock_start + n):
        for j in range(lock_start, lock_start + n):
            grid[i][j] = lock[i - lock_start][j - lock_start]

    return grid


def rotate_key(key):
    new_key = [[0] * len(key) for _ in range(len(key))]

    for i, k_row in enumerate(key):
        for j, k in enumerate(k_row):
            new_key[i][j] = key[len(key) - 1 - j][i]
            # (2, 0), (1, 0), (0, 0)
            # => (0, 0), (0, 1), (0, 2)

    return new_key


def get_grid(m, n):
    length = 2 * (m - 1) + n
    grid = [[0] * length for _ in range(length)]
    return grid


def set_key(grid, key, key_i, key_j):
    m = len(key)

    for i in range(key_i, key_i + m):
        for j in range(key_j, key_j + m):
            grid[i][j] += key[i - key_i][j - key_j]


def is_zero_or_two_exist_in_lock(grid, n, lock_i, lock_j):
    for i in range(lock_i, lock_i + n):
        for j in range(lock_j, lock_j + n):
            if grid[i][j] == 0 or grid[i][j] == 2:
                return True

    return False


def solution(key, lock):
    m = len(key)
    n = len(lock)
    length = 2 * (m - 1) + n

    # 4방향
    for k in range(4):
        key = rotate_key(key)

        for i in range(length - m + 1):
            for j in range(length - m + 1):
                grid = get_grid(m, n)
                set_lock(grid, key, lock)
                set_key(grid, key, i, j)

                if not is_zero_or_two_exist_in_lock(grid, n, m - 1, m - 1):
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
