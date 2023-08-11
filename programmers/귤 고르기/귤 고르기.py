from collections import defaultdict


def get_min_kind(arr: list, limit: int):
    sums = 0
    kind = 0

    for key, value in arr:
        sums += value
        kind += 1

        if sums >= limit:
            break

    return kind


def solution(k, tangerine):
    t_dict = defaultdict(int)

    for t in tangerine:
        t_dict[t] += 1

    t_arr_desc = sorted(t_dict.items(), key=lambda x: x[1], reverse=True)

    return get_min_kind(t_arr_desc, k)


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))

# 조합? -> X

# 겹치는 귤은 가능한 살려 둬야 한다

# [1, 2, 2, 3, 3, 4, 5, 5]
# 겹치는게 없는 귤 제거

# 제거할 필요 없이 갯수가 많은 귤부터 더해 나간다
# 그리고 k 이상 귤이 모이면 그게 정답이 된다
# 많은 귤부터 그리디 하게 넣어서
# 이게 최소 종류로 귤을 넣을 수 있는 방식이다

# 참고
# https://greenhelix.tistory.com/231
# https://stackoverflow.com/questions/10194713/sorting-a-defaultdict-by-value-in-python
# https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
