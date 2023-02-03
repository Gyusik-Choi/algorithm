# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = []
    for j in move:
        for k in range(len(board)):
            if board[k][j-1] != 0:
                stack.append(board[k][j-1])
                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                board[k][j-1] = 0
                break
    return answer
