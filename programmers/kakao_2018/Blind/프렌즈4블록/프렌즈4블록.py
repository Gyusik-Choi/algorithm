def solution(m, n, board):
    answer = 0
    # 문자열을 리스트 요소화해서 2차원 배열로 바꿈
    # 배열 -90도 회전(빈 자리에 블록 옮기기에 용이해 보여서)
    # 우측 90도(참고용)
    # arr90 = list(zip(*arr[::-1]))
    # -90도(실제 사용할 배열)
    # arr270 = list(zip(*arr))[::-1])
    # 단 위는 튜플이 되서 값을 바꿀수가 없어서 list 로 바꿔준다.
    arr270 = list(map(list, zip(*board)))[::-1]
    # 겹치는 값 체크할 추가 배열
    check_arr = [[0] * len(arr270[0]) for _ in range(len(arr270))]

    # 겹치는 값이 없을 때 까지 돌린다.
    while True:
        result = True
        # 2 x 2 체크해서 모두 같으면 체크 배열에 1 넣어준다. 더해주는 건 안 된다. 연속으로 겹치는 부분 발생시 2가 되므로. 그걸 막아주는 장치.
        for i in range(len(arr270) - 1):
            for j in range(len(arr270[0]) - 1):
                if arr270[i][j] != 0:
                    if arr270[i][j] == arr270[i][j + 1] == arr270[i + 1][j] == arr270[i + 1][j + 1]:
                        result = False
                        check_arr[i][j] = check_arr[i][j + 1] = check_arr[i + 1][j] = check_arr[i + 1][j + 1] = 1

        # result 가 True 이면 더 이상 겹치는 값이 나오지 않았으므로 끝낸다.
        # result 를 맨 마지막에 검사하면 밑의 연산을 할 필요가 없음에도 또 수행해야 하므로 여기서 검사해서 추가적인 연산을 막는다.
        if result:
            return answer

        # 한번 다 돌고 나면 체크 배열의 1들 모두 더해주고, 다시 0으로 만든다.
        # 한번 다 돌고 나면 arr270 배열에서 겹쳤던 부분은 0으로 만든다.
        for i in range(len(check_arr)):
            for j in range(len(check_arr[0])):
                if check_arr[i][j] == 1:
                    answer += 1
                    check_arr[i][j] = 0
                    arr270[i][j] = 0

        # 비어있는 부분에 하나씩 요소 옮긴다.
        for i in range(len(arr270)):
            for j in range(len(arr270[0]) - 1, -1, -1):
                if arr270[i][j] != 0:
                    for k in range(len(arr270[0]) - 1, j, -1):
                        if arr270[i][k] == 0:
                            arr270[i][k] = arr270[i][j]
                            arr270[i][j] = 0


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
