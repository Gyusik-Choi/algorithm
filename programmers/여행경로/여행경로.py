from collections import defaultdict


def solution(tickets):
    def dfs(departure, visited, history):
        if len(history) == len(tickets) + 1:
            answer.extend(history)
            return

        if answer:
            return

        # 키를 arrival 이 아니라 idx 로 조회
        for idx, arrival in enumerate(routes[departure]):
            if visited[departure][idx]:
                continue

            visited[departure][idx] = True
            history.append(arrival)
            dfs(arrival, visited, history)
            visited[departure][idx] = False
            history.pop()

    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        start, end = ticket
        routes[start].append(end)

    for value in routes.values():
        value.sort()

    # 값으로 딕셔너리를 사용 했으나
    # 중복 티켓 문제 때문에 리스트로 바꿨다
    # 키 마다 딕셔너리를 값으로 가지는 방식에서
    # 키 마다 리스트를 값으로 갖는 방식으로 바꿈
    # 예를 들어 tickets 이
    # ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"] 라면
    # visit 의 값이 만약 딕셔너리고
    # 이 딕셔너리의 키를 도착지, 값을 bool 로 설정하면
    # 동일한 키를 딕셔너리에 중복으로 넣을 수 없다
    # ICN 에서 갈 수 있는 세개의 "AAA" 가
    # 모두 하나로 처리 된다
    # 중복 티켓을 처리할 수 없다
    visit = dict()

    for key, value in routes.items():
        visit[key] = [False] * len(value)

    dfs('ICN', visit, ['ICN'])
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

# 반례
# https://school.programmers.co.kr/questions/10332
print(solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]))
# => ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO']
# 아직 방문 못한 도시가 있지만 다 못돌고 다음 코스로 넘어갈 수 있다
# 'ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO' 까지 왔을 때
# 'COO' 에서 'BOO' 로 가면 'BOO' 에서 더 이상 갈 수 있는 도시가 없지만
# 'DOO' 에서 'COO' 로 가는 루트가 남는다
# 루트가 계속 이어지려면
# 'COO' 에서 'BOO' 가 아닌 'DOO' 로 가야 모든 방문 가능한 도시를
# 끊기지 않고 이어서 방문할 수 있다

# 반례
# https://school.programmers.co.kr/questions/33058
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]))
# => ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

# 참고
# https://ljhyunstory.tistory.com/107
# https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-%EC%BD%94%EB%93%9C-%ED%92%80%EC%9D%B4-%EB%81%84%EC%A0%81%EB%81%84%EC%A0%81
