import sys


def avg(lst, n):
    return round(sum(lst) / n)


def center(lst, n):
    idx = len(lst) // 2
    lst.sort()
    return lst[idx]


def mode(lst):
    dic = {}
    for j in range(len(lst)):
        if lst[j] not in dic:
            dic[lst[j]] = 0
        else:
            dic[lst[j]] += 1

    dic_to_lst = sorted(dic.items(), reverse=True, key=lambda x: x[1])
    print(dic_to_lst)

    if len(dic_to_lst) > 1:
        key_lst = dic_to_lst[:2]
        if key_lst[0][1] == key_lst[1][1]:
            return key_lst[1][0]
        else:
            return key_lst[0][0]
    else:
        return dic_to_lst[0][0]


def scope(lst):
    max_num = max(lst)
    min_num = min(lst)
    return max_num - min_num


N = int(input())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

print(avg(arr, N))
print(center(arr, N))
print(mode(arr))
print(scope(arr))
