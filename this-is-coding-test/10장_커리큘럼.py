import copy
from collections import deque


def topology_sort():
    # 다른 방법이 없을까 고민했지만 답안에도 이렇게 깊은 복사를 수행해서 안심했다
    time = copy.deepcopy(subject_time)
    deq = deque()

    for k in range(1, N + 1):
        if in_degree[k] == 0:
            deq.append(k)

    while deq:
        start = deq.popleft()
        for end in prior_subjects[start]:
            in_degree[end] -= 1
            if in_degree[end] == 0:
                time[end] = max(time[end], time[end] + time[start])
                deq.append(end)

    return time


N = int(input())
# 선수 강의 수
in_degree = [0] * (N + 1)
# 선수 강의 정보
prior_subjects = [[] for _ in range(N + 1)]
# 강의별 시간 정보
subject_time = [0] * (N + 1)

for i in range(1, N + 1):
    subject = list(map(int, input().split()))
    subject.pop()
    subject_time[i] = subject[0]

    if len(subject) > 1:
        in_degree[i] += len(subject) - 1
        for j in range(1, len(subject)):
            prior_subjects[subject[j]].append(i)

answer = topology_sort()
for i in range(1, len(answer)):
    print(answer[i])

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
# => (세로로 출력한다) 10 20 14 18 17

# 5
# 10 -1
# 10 1 3 -1
# 20 -1
# 15 3 -1
# 10 2 4 -1
# => (세로로 출력한다) 10 30 20 35 45

# 큐 방식에서 출발점을 어떻게 찾는게 좋을까?
# => 출발점은 당연히 in_degree 가 0인 지점이다(이를 이해해야 큐 방식의 위상 정렬을 수행할 수 있다)

# in_degree 최소값이 여러개 일 수 있는데 이때 어떻게 하는게 좋을지 고민이다
# => 출발점은 in_degree 가 0인 지점이 하나건 둘이건 먼저 큐에 넣고 수행하면 되는거라 문제될게 없다

# topology_sort 함수 안에
# end 값에 Unexpected type(s): (list) Possible type(s): (_SupportsIndex) (slice)
# 음영이 생기면서 커서를 올리면 이런 에러가 뜨는데 왜 뜨는 건지 잘 모르겠다...
