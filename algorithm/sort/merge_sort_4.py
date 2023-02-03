def merge_sort(low, high):
    if high - low < 1:
        return
    mid = (low + high) // 2
    merge_sort(low, mid)
    merge_sort(mid + 1, high)

    l = low
    m = mid + 1
    temp = []
    while l <= mid and m <= high:
        if arr[l] < arr[m]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[m])
            m += 1

    # 위에서 while 문을 처리하고 남은 나머지 부분을 처리하는데
    # while 문을 탈출할 때 둘 중 하나는 만족하고 하나는 만족하지 못했다
    # 둘 중 무엇을 만족했는지 모르기 때문에 일단 둘 다 처리를 하되
    # while 문을 불필요하게 검증하지 않기 위해 if 문을 추가했지만
    # while 문으로도 조건을 검증할 수 있어서 if 문은 없어도 무방하다
    # if 문은 l 이나 m 중에 1개는 각각 mid 나 high 보다 큰 상황이라 l > mid, m > high 라는 조건을 달았다
    if m > high:
        while l <= mid:
            temp.append(arr[l])
            l += 1

    if l > mid:
        while m <= high:
            temp.append(arr[m])
            m += 1

    t = 0
    while t < len(temp):
        arr[low + t] = temp[t]
        t += 1


arr = [2, 1, 5, 4, 3]
merge_sort(0, len(arr) - 1)
print(arr)

# 참고
# https://www.daleseo.com/sort-merge/
