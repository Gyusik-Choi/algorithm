def quick_sort(f):
    if len(f) <= 1:
        return f
    pivot = len(f) // 2
    small = []
    same = []
    big = []
    for i in range(len(f)):
        if f[i][1] > f[pivot][1]:
            big.append(f[i])
        elif f[i][1] == f[pivot][1]:
            same.append(f[i])
        else:
            small.append(f[i])
    arr = quick_sort(big) + same + quick_sort(small)
    return arr


def solution(N, stages):
    stages = sorted(stages)
    arr = []
    cnt_arr = [0]
    users = len(stages)
    for i in range(1, N + 1):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i:
                cnt += 1
        if i not in stages:
            arr.append([i, 0])
        else:
            users -= cnt_arr[-1]
            cnt_arr.append(cnt)
            arr.append([i, cnt / users])

    # stages = sorted(stages)
    # dummy = list(range(1, N + 1))
    # user_dict = dict.fromkeys(dummy, 0)
    # for i in stages:
    #     if i in user_dict:
    #         user_dict[i] += 1
    #
    # failure = []
    # users = len(stages)
    # for i in user_dict:
    #     if i == 1:
    #         failure.append([1, user_dict[i] / users])
    #     else:
    #         users -= user_dict[i - 1]
    #         failure.append([i, user_dict[i] / users])
    ans = quick_sort(arr)
    ans_arr = []
    for i in ans:
        ans_arr.append(i[0])
    print(ans_arr)


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4, 4, 4, 4, 4])
