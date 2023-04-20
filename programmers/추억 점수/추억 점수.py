from collections import defaultdict


def solution(name, yearning, photo):
    # defaultdict 안에 디폴트 값으로 사용할 타입을 지정해 줘야 한다
    name_info = defaultdict(int)

    for i, name in enumerate(name):
        name_info[name] = yearning[i]

    sums = [0] * len(photo)

    for i, one_photo in enumerate(photo):
        for j, p in enumerate(one_photo):
            sums[i] += name_info[p]

    return sums


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))

