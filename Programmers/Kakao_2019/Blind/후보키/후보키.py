from itertools import combinations


# 조합 구하는 함수
def com(arr, length):
    items_lst = []
    for i in list(combinations(arr, length)):
        items_lst.append(i)
    return items_lst


def solution(relation):
    cnt = 0
    length = len(relation[0])
    # relation 의 요소값을 직접 사용하기 보다는 인덱스를 통해 확인
    lst = list(range(length))
    # check 배열에 유일성, 최소성 갖는 것 담음
    check = []
    # 길이별로 조합 구한다.
    for j in range(1, length + 1):
        comb = com(lst, j)
        for item in comb:
            # 유일성 체크
            # check 에 들어간 요소들을 하나씩 꺼내서 후보키 후보와 비교한다.
            uniqueness = True
            candidate = []
            for che in check:
                item_cnt = 0
                for c in che:
                    if c in item:
                        item_cnt += 1
                if item_cnt == len(che):
                    uniqueness = False
                    break
            # 유일성 체크 통과했다면
            if uniqueness:
                for i in range(len(relation)):
                    candid = []
                    for each_item in item:
                        candid.append(relation[i][each_item])
                    # 튜플로 변환해서 배열에 넣으면 set 함수로 중복 여부 체크할 수 있다.
                    candid = tuple(candid)
                    candidate.append(candid)
                # 중복 되지 않는다면
                if len(candidate) == len(set(candidate)):
                    cnt += 1
                    check.append(item)
    return cnt


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
print(solution([['a', 'b', 'c'], [1, 'b', 'c'], ['a', 'b', 4], ['a', 5, 'c']]))
print(solution([['a', 1, 4], [2, 1, 5], ['a', 2, 4]]))
print(solution([["b", 2, "a", "a", "b"], ["b", 2, 7, 1, "b"], [1, 0, "a", "a", 8], [7, 5, "a", "a", 9], [3, 0, "a", "f", 9]]))
