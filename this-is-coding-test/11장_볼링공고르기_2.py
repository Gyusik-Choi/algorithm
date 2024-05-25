def cancel_visit(temp_comb, i):
    temp_comb.pop()
    visited[i] = False


def visit(temp_comb, i):
    temp_comb.append(i)
    visited[i] = True


def combination(balls_limit, balls, temp_comb):
    if balls_limit == balls:
        combs.append(temp_comb[:])
        return

    for i in range(N):
        if not visited[i]:
            # temp_comb 에 볼링공 없으면 바로 넣고,
            # temp_comb 에 볼링공 있으면 temp_comb 에 있는 볼링공 보다 배열 인덱스 값이 더 크면서 볼링공 번호가 같지 않으면 넣는다
            # (and 가 or 보다 우선 순위가 높지만 가독성을 위해 괄호 표시함)
            if not temp_comb or (temp_comb[-1] < i and weights[temp_comb[-1]] != weights[i]):
                visit(temp_comb, i)
                combination(balls_limit, balls + 1, temp_comb)
                cancel_visit(temp_comb, i)


N, M = map(int, input().split())
weights = list(map(int, input().split()))

combs = []
visited = [0] * N
# 볼링공 갯수 제한, 볼링공 갯수, 볼링공 조합
combination(2, 0, [])

print(len(combs))

# 5 3
# 1 3 2 3 2
# => 8

# 8 5
# 1 5 4 3 2 4 5 2
# => 25
