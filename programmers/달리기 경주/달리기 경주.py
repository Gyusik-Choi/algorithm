def solution(players, callings):
    # 위치, 선수
    i = {i: p for i, p in enumerate(players)}

    # 선수, 위치
    p = {p: i for i, p in enumerate(players)}

    for player in callings:
        idx = p[player]
        pre_idx = idx - 1
        pre_player = i[pre_idx]

        p[player] -= 1
        p[pre_player] += 1
        i[idx], i[pre_idx] = i[pre_idx], i[idx]

    return list(i.values())


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
