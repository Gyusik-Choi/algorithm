N = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

# 그룹 총 수
number_of_groups = 0
# 기준점
i = 0
while i < N:
    # 기준점부터 시작
    j = i
    # 기준점부터 시작하므로 일단 그룹 인원 1명은 확보한 상황
    group = 1
    while j < N:
        # 그룹 인원이 공포도보다 크거나 같으면 그룹의 요건을 충족했다
        # 그룹 총 수에 1을 더해주고 안쪽 while 문을 종료
        if group >= adventurers[j]:
            number_of_groups += 1
            break
        # 그룹 인원이 공포도보다 작으므로 그룹에 인원을 더 넣을 수 있다
        # 현재 인원외에 1명을 미리 추가하기 위해 group 에 1을 더한다
        # j에 1을 더해서 다음 인덱스로 넘어간다
        else:
            group += 1
            j += 1
    # j 인덱스 + 1
    # 지금까지 구한 j 다음에서 i 가 시작될 수 있도록 한다
    i = j + 1

print(number_of_groups)

# 5
# 2 3 1 2 2
# => 2

# 9
# 1 2 3 3 3 4 4 5 6
# => 2

# 9
# 1 1 2 2 3 4 5 5 6
# => 3

# 9
# 10 10 10 10 10 10 10 10 10
# => 0
