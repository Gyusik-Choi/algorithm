def solution(board):
    n, m = len(board), len(board[0])
    # board 와 똑같은 값을 갖는 dp 리스트 초기화
    dp = list(map(lambda x: x, list(map(lambda x: x, board))))
    # 초기값을 0으로 하면
    # board 가 [[1]] 인 경우
    # 리턴 값이 1이 아닌 0이 된다
    # 이를 막기 위해
    # board 의 첫번째 값으로 초기화
    answer = board[0][0]

    for i in range(1, n):
        for j in range(1, m):
            if not dp[i][j]:
                continue
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            answer = max(answer, dp[i][j])

    return answer * answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1]]))

# 참고
# https://soobarkbar.tistory.com/164
