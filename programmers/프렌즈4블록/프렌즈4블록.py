def solution(m, n, board):
    def is_four(y, x):
        if not board[y][x]:
            return False

        prev = board[y][x]
        for a in range(y, y + 2):
            for b in range(x, x + 2):
                if prev != board[a][b]:
                    return False
        return True

    def remove_blocks(y, x):
        for a in range(y, y + 2):
            for b in range(x, x + 2):
                board[a][b] = ""

    def fill_empty_blocks():
        for b in range(n):
            for a in range(m - 2, -1, -1):
                # 본인이 빈칸이 아닌 경우 마지막 빈칸을 찾는다
                # 빈칸이 없으면 0 을 리턴
                if not board[a][b]:
                    continue
                y = find_last_empty_block(a + 1, b)
                if not y:
                    continue
                # 기존 자리는 빈칸으로 만들고 이동
                char = board[a][b]
                board[a][b] = ""
                board[y][b] = char

    def find_last_empty_block(y, x):
        for a in range(m - 1, y - 1, -1):
            if not board[a][x]:
                return a
        return 0

    def count_to_be_removed(blocks):
        non_duplicated_blocks = set()
        for bloc in blocks:
            for a in range(bloc[0], bloc[0] + 2):
                for b in range(bloc[1], bloc[1] + 2):
                    k = str(a) + " " + str(b)
                    non_duplicated_blocks.add(k)
        return len(non_duplicated_blocks)

    board = list(map(lambda x: list(x), board))
    answer = 0

    while True:
        four_blocks = []

        for i in range(m - 1):
            for j in range(n - 1):
                if is_four(i, j):
                    four_blocks.append([i, j])

        if not four_blocks:
            break

        answer += count_to_be_removed(four_blocks)

        for block in four_blocks:
            remove_blocks(block[0], block[1])
        fill_empty_blocks()

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
