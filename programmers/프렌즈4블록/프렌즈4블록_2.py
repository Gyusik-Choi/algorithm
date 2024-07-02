def solution(m, n, board):
    board = [list(b) for b in board]

    while True:
        four_blocks = []

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != "":
                    four_blocks.append([i, j])

        if not four_blocks:
            break

        for i, j in four_blocks:
            board[i][j] = board[i + 1][j] = board[i][j + 1] = board[i + 1][j + 1] = ""

        for _ in range(m - 1):
            for i in range(m - 1):
                for j in range(n):
                    if not board[i + 1][j]:
                        board[i + 1][j], board[i][j] = board[i][j], ""

    return sum(b.count("") for b in board)


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
