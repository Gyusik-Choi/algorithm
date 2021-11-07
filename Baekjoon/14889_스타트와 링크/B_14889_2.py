def count_abilities(start, link):
    start_sums = 0
    link_sums = 0

    for i in range(len(start) - 1):
        start_one = start[i]
        link_one = link[i]
        for j in range(i + 1, len(start)):
            start_two = start[j]
            link_two = link[j]

            start_sums += abilities[start_one][start_two] + abilities[start_two][start_one]
            link_sums += abilities[link_one][link_two] + abilities[link_two][link_one]

    return abs(start_sums - link_sums)


def get_link_team():
    link_team_candidates = [True for _ in range(N)]
    for i in range(N // 2):
        link_team_candidates[start_team[i]] = False

    link_team = []
    for idx, candidate in enumerate(link_team_candidates):
        if candidate:
            link_team.append(idx)

    return link_team


def get_start_team(idx):
    global answer
    if idx == N // 2:
        link_team = get_link_team()
        ability_difference = count_abilities(start_team, link_team)
        answer = min(answer, ability_difference)
    else:
        for i in range(N):
            if start_team:
                if start_team[-1] < i:
                    start_team.append(i)
                    get_start_team(idx + 1)
                    start_team.pop()
            else:
                if i == 0:
                    start_team.append(i)
                    get_start_team(idx + 1)
                    start_team.pop()


N = int(input())
abilities = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
start_team = []
get_start_team(0)

print(answer)

# N / 2의 인원으로 스타트 팀을 구하면 나머지는 링크 팀이 된다
# 스타트 팀과 링크 팀을 각각 이중 for 문을 통해 능력치 총합을 구한다
# 능력치 총합의 차이를 비교하고 기존의 최소값과 비교한다
