from collections import deque


def solution(people, limit):
    people.sort()
    deq = deque()

    for p in people:
        deq.append(p)

    cnt = 0
    on_board = 0

    while deq:
        p1 = deq.popleft()
        on_board += 1

        while deq:
            p2 = deq.pop()

            # p1, p2 를 1개의 구명 보트에 태울 수 있음
            if p1 + p2 > limit:
                cnt += 1
                continue

            # p2 만 구명 보트에 태운다
            cnt += 1
            on_board = 0
            break

        # p1 + p2 <= limit 조건을 만족 못하고
        # 안쪽 while 문을 다 돌고 끝나면
        # 바깥쪽 while 문의 p1 이 남아 있다
        if on_board:
            cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([10, 20, 30, 40], 50))
