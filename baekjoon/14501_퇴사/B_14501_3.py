def is_consult_possible(day, term):
    return day + term <= N


def check_post_consult(consult):
    term, cost = consult_info[consult]

    # 다음 상담 가능한 날짜
    post_consult = consult + term

    if post_consult >= N:
        return

    # 해당 날짜 부터 이후 날짜 모두 탐색
    for day in range(post_consult, N):
        post_term, post_cost = consult_info[day]

        # 해당 날짜 자체가 상담 가능한 날인지
        if not is_consult_possible(day, post_term):
            continue

        # cost 가 아닌 dp[consult] 로 비교 해야 한다
        # 상담 하려는 날짜의 dp 배열 값을 갱신 할때
        # 상담 하려는 날짜는 그 날짜 자체의 상담 비용이 필요 하지만
        # 기준 날짜는 dp 배열 값을 사용 해야 한다
        if dp[day] >= dp[consult] + post_cost:
            continue

        dp[day] = dp[consult] + post_cost


N = int(input())
consult_info = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for start, c in enumerate(consult_info):
    period, pay = c

    if not is_consult_possible(start, period):
        continue

    dp[start] = pay

for start, c in enumerate(consult_info):
    check_post_consult(start)

print(max(dp))

# 완전 탐색 + DP
# 모든 상담 일정을 탐색
# 특정 상담 일정 기간 충족한 날짜 이후의 모든 날짜들 탐색 해서 갱신
# README 에 작성한 기존 풀이와 유사 하지만 조금 다른 점은
# 기존 풀이는 현재 상담을 기준 하여 이전의 상담을 봤다면
# 이번 풀이는 현재 상담을 기준 하여 이후의 상담을 본다
