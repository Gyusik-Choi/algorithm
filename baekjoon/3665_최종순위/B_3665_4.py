from collections import deque
import sys


def is_cycle():
    for idx in range(1, n + 1):
        if level[idx]:
            return True

    return False


def topology_sort():
    answer = []
    deq = deque()

    for idx in range(1, n + 1):
        if level[idx]:
            continue
        deq.append(idx)

    while deq:
        start = deq.popleft()

        answer.append(start)

        for end in range(1, n + 1):
            if grade[start][end]:
                level[end] -= 1

                if not level[end]:
                    deq.append(end)

    if is_cycle():
        return 'IMPOSSIBLE'

    return ' '.join(list(map(str, answer)))


t = int(input())
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    m = int(input())

    # 간선 간의 선후 관계를 나타낸다
    # 상대적 선후 관계를 나타낸다
    # 누가 누구 보다 우선 순위가 높은지 알 수 있으나
    # 몇 단계나 우선 순위가 높은지 알 수 없다
    # 이는 진입 차수로 알 수 있다
    # 단 진입 차수 만으로는 나머지 요소들 간의 상대적 순위를
    # 제대로 파악할 수 없다
    # grade 없이 순위를 바꾸기 위해 level 만 바꾸면
    # 일관성 있는 정보인지 파악하기 어렵다
    # 나머지 요소들 간의 상대적 순위를 깨지 않으면서
    # 서로 간의 상대적 순위를 바꿀 수 있는지 여부를
    # 제대로 파악할 수 없다
    # 예를 들어 level = [1, 2, 3, 4, 5] 라고 할때
    # 2번, 4번 인덱스의 상대 순위를 바꾸기 위해 이 둘을 바꾸면
    # [1, 4, 3, 2, 5] 가 되는데 얼핏 보면 문제가 없는 것 같다
    # 그러나 인덱스 3의 값이
    # 기존의 2번 인덱스 보다 높고
    # 4번 인덱스 보다 낮아야 한다는
    # 조건을 충족할 수 없다
    grade = [[0] * (n + 1) for _ in range(n + 1)]
    # 진입 차수
    level = [0] * (n + 1)

    for i in range(n - 1):
        high = last_year[i]

        for j in range(i + 1, n):
            low = last_year[j]
            level[low] += 1
            grade[high][low] = 1

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())

        if grade[a][b]:
            grade[a][b] = 0
            level[b] -= 1

            grade[b][a] = 1
            level[a] += 1
        else:
            grade[b][a] = 0
            level[a] -= 1

            grade[a][b] = 1
            level[b] += 1

    sys.stdout.write(topology_sort() + "\n")

# 처음에 level 만 가지고 풀이를 하려 했다
# 순위가 변동이 되면 서로의 level 값을 바꾸려 했다
# level 값을 서로 바꿔줄 때 문제점은
# 순위가 바뀐다고 했을 때
# 순위가 바뀌지 않는 정점들 간의 선후 관계는 변함이 없어야 한다
# 예를 들어 작년 순위가 5 4 3 2 1 이고
# 상대적인 등수가 바뀐 팀이 2 4 라고 할때
# (5, 2), (3, 2), (1, 2), (5, 4), (4, 3), (4, 1)
# 해당 팀들 간의 선후 관계가 변함이 없어야 한다
#
# level 만 가지고 풀이를 하면 5 4 3 2 1 순위에서
# 2 4 의 등수를 바꾸는게 가능하게 풀이가 된다
# 그러나
# 실제로는 사이클이 생기기 때문에 IMPOSSIBLE 이 정답이 되야 한다
# 2와 4를 바꾸면 5 2 3 4 1 이 되는데 이럴 경우
# (2, 3), (3, 4) 의 상대적 순위가 바뀌었다
# 3은 4보다 상대적 순위가 낮고 3은 2보다 상대적 순위가 높아야 하는데
# 이것을 충족하지 못한다
# 3이 4보다 상대적 순위가 낮아야 해서 5 2 4 3 1 이 되는데
# 3이 2보다 상대적 순위가 높아야 해서 5 4 3 2 1 이 되면
# 원래대로 되고 이것의 무한 반복이 돼서 사이클이 생긴다
#
# 그래서 level 만으로는 선후 관계를 제대로 파악할 수 없다
# 5 4 3 2 1 에서 5와 1의 절대적 순위 차이는
# 진입 차수로 알 수 있는 것이고
# 5와 1의 둘 사이 자체의 관계는 5가 1보다
# 상대적 순위가 높다는 것 뿐이다
#
# 참고
# https://zoosso.tistory.com/369
