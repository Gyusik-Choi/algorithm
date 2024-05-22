N, M = map(int, input().split())
balls = list(map(int, input().split()))

# 무게는 최소 1부터 최대 10까지 존재 가능
weights = [0] * 11

for idx, ball in enumerate(balls):
    weights[ball] += 1

total = N
combinations = 0

# 입력 받는 무게는 1부터 M까지
for weight in range(1, M + 1):
    # 총 공 갯수에 동일한 무게를 갖는 공 갯수 제거
    total -= weights[weight]
    # 총 볼링공 갯수 * 해당 볼링공 갯수
    # 동일한 번호의 공은 자신과 동일한 번호 외에 나머지 번호와 각각의 조합 갖는다
    combinations += total * weights[weight]

print(combinations)
