# 기존의 counting_sort.py 보다 코드가 더 간단하다
# 기존의 방법과 마찬가지로
# 최대값 + 1 길이 만큼의 배열(max_lst)을 만들고
# 정렬 대상의 원소를 인덱스로 사용하여 갯수를 더해줬다
# 그리고 max_lst 의 각 원소들의 값만큼
# 인덱스 값을 정렬된 값을 담을 배열(sorted_lst)에 넣어주면 끝이다
import copy


def counting_sort2(lst):
    max_lst = [0] * (max(lst) + 1)

    for i in range(len(lst)):
        max_lst[lst[i]] += 1

    sorted_lst = []

    for i in range(len(max_lst)):
        for j in range(max_lst[i]):
            sorted_lst.append(i)

    return sorted_lst


arr = [2, 1, 7, 6, 7, 5, 7, 4, 3]
print(counting_sort2(copy.deepcopy(arr)))
