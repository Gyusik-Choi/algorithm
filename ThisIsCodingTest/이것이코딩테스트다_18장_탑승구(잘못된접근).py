def binary_search(target, start, end):
    mid = (start + end) // 2

    if mid == target:
        if visited[mid] == 0:
            return mid
        # start 가 end 보다 크거나 같을 경우의 탈출 조건은 상위에 없는 대신
        # mid == target 인 상황에서
        # target, start, end 모두 1씩 줄여서
        # 계속 mid == target 에 들어올 수 있도록 한다
        return binary_search(target - 1, start - 1, end - 1)

    if mid > target:
        return binary_search(target, start, mid)
    return binary_search(target, mid + 1, end)


G = int(input())
P = int(input())

gates = []
for _ in range(P):
    g = int(input())
    gates.append(g)

answer = 0
visited = [0] * (G + 1)
for gate in gates:
    if visited[gate] == 0:
        visited[gate] = 1
        answer += 1
    else:
        if gate - 1 == 0:
            break

        idx = binary_search(gate, 0, gate)

        # idx 가 0이 나올 수 있는데 이때는 종료 시킨다
        if idx == 0:
            break

        visited[idx] = 1
        answer += 1

print(answer)

# 4
# 3
# 4
# 1
# 1
# => 2

# 4
# 3
# 4
# 4
# 4
# => 3

# 4
# 5
# 4
# 4
# 4
# 4
# 4
# => 4

# 5
# 5
# 3
# 5
# 3
# 1
# 3
# => 5

# 5
# 5
# 3
# 5
# 3
# 1
# 3
# => 4
