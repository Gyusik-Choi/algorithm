def get_permutations(limit, permutations, perm):
    if len(perm) == limit:
        permutations.append(perm[:])
        return

    for i in range(limit):
        if i not in perm:
            perm.append(i)
            get_permutations(limit, permutations, perm)
            perm.pop()

    return permutations


def get_visit_num(cur, dungeons, permutation):
    cnt = 0

    for p in permutation:
        min_required_fatigue, consumption_fatigue = dungeons[p]

        # 최소 피로도 만족 X
        if cur < min_required_fatigue:
            return cnt

        cur -= consumption_fatigue
        cnt += 1

    return cnt


def solution(k, dungeons):
    permutations = get_permutations(len(dungeons), [], [])
    answer = 0

    for perm in permutations:
        answer = max(answer, get_visit_num(k, dungeons, perm))

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
