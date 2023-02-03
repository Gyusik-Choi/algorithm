import sys


n = int(input())
# 정렬된 회의 시간을 기준으로 첫번째 회의는 포함하고 시작할거라 cnt 를 1로 설정
cnt = 1
meetings = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append([s, e])

# 회의를 일찍 끝나는 순서로 정렬하되 끝나는 순서가 같으면 일찍 시작하는 순서로 정렬되도록 한다
# x[0] 을 지정하지 않으면 끝나는 순서가 같은 회의들은 입력된 순서대로만 정렬된다
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

# 정렬된 첫번째 회의 시작 시간(없어도 무방)
prior_start = meetings[0][0]
# 정렬된 첫번째 회의 끝나는 시간
prior_end = meetings[0][1]

# 두번째 회의부터 for 문을 돌면서 탐색
for i in range(1, len(meetings)):
    # 회의 시작 시간
    start = meetings[i][0]
    # 회의 끝나는 시간
    end = meetings[i][1]
    # 앞선 회의가 끝나는 시간보다 이번 회의의 시작 시간이 같거나 더 커야 회의실을 잡을 수 있다
    if prior_end <= start:
        cnt += 1
        # (시작 시간은 안바꿔줘도 무방)
        prior_start = start
        # 회의장을 받았으므로 회의 끝나는 시간을 이번 회의의 끝나는 시간으로 바꿔줌
        prior_end = end

print(cnt)
