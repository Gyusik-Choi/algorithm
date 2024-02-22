def get_start_matrix(r, c):
    matrix = [[i * c + j + 1 for j in range(c)] for i in range(r)]
    return matrix


def get_copied_matrix(matrix):
    r, c = len(matrix), len(matrix[0])
    copied_matrix = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            copied_matrix[i][j] = matrix[i][j]

    return copied_matrix


def solution(rows, columns, queries):
    matrix = get_start_matrix(rows, columns)
    min_nums = []
    print(matrix)
    for query in queries:
        copied_matrix = get_copied_matrix(matrix)

        y1, x1, y2, x2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        min_num = 10001

        # left -> right
        for x in range(x2 - x1):
            matrix[y1][x1 + x + 1] = copied_matrix[y1][x1 + x]
            min_num = min(min_num, matrix[y1][x1 + x + 1])

        # top -> bottom
        for y in range(y2 - y1):
            matrix[y1 + y + 1][x2] = copied_matrix[y1 + y][x2]
            min_num = min(min_num, matrix[y1 + y + 1][x2])

        # right -> left
        for x in range(x2 - x1):
            matrix[y2][x2 - x - 1] = copied_matrix[y2][x2 - x]
            min_num = min(min_num, matrix[y2][x2 - x - 1])

        # bottom -> top
        for y in range(y2 - y1):
            matrix[y2 - y - 1][x1] = copied_matrix[y2 - y][x1]
            min_num = min(min_num, matrix[y2 - y - 1][x1])

        min_nums.append(min_num)

    return min_nums


# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# print(solution(100, 97, [[1, 1, 100, 97]]))

print(solution(2, 3, [[1, 2, 2, 3]]))
print(solution(3, 2, [[1, 2, 2, 2]]))
print(solution(4, 4, [[1, 2, 2, 3]]))

# 참고
# https://school.programmers.co.kr/questions/25770
