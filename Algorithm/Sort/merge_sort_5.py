# high 를 기존에는 arr 의 마지막 index 보다 1 크게 잡은 방식으로 해서 이번에는 high 를 마지막 index 와 같게 설정했다
# 간단하게 바꿀 줄 알았는데 생각보다 어려웠고 병합 정렬을 다시 공부해볼 수 있었다

# 병합 정렬을 수행하기 위해 배열을 가장 작은 단위로 쪼개야 한다
# 절반씩 나눠가기 위해 low 와 high 의 중간 인덱스 mid 를 구해서 low 부터 mid 까지, mid + 1부터 high 까지로 각각 나눈다.
# (기존 코드는 low 부터 mid 지만 실제로는 mid 는 포함하지 않는 범위라 low 부터 mid - 1 까지고 mid 부터 high 도 mid 부터 high - 1 까지였다)
# 재귀적으로 계속 나눠서 더 이상 나누어 질 수 없을 때까지 진행한다

# [2, 1, 4, 3] 라면 [2], [1], [4], [3] 이렇게 나눠야 하므로 리턴 조건을 high - low < 1로 잡았다
# (최대로 나눴을 때 low 가 [2] high 가 [1]이 되어야 한다. 나누는 merge_sort 코드가 재귀적으로 두 줄로 구성된다. 즉 나누는 부분의 왼쪽과 오른쪽을 각각 담당하게 된다.
# return 조건에 걸리는 부분은 low, high 파라미터에 들어온 low, mid 혹은 mid + 1, high 인자가 된다.
# 위에서 얘기한 것처럼 low 가 [2], high 가 [1]이 되려면
# 재귀를 도는 두개 merge_sort 코드의 모든 인자가 low, mid, mid + 1, high 이렇게 있을 때 low 가 0 high 가 1이 되야 한다는 뜻이다.
# low = 0, mid = 0, mid + 1 = 1, high = 1 이 되야 return 조건을 만족할 수 있다. 그래서 if high - low < 1 일때 return 을 한다)
# (기존 코드는 high 가 포함되지 않는 범위라 high - low < 2로 잡았었다)

# 다 나누면 비교를 진행하게 된다
# l 이라는 변수는 low, m 이라는 변수는 m + 1로 잡고서 l 이 mid 보다 작거나 같고 m 이 high 보다 작거나 같을 동안 계속 비교한다
# 2, 1 를 비교하는 상황이라면 low 는 0, mid 는 0, high 는 1 이다. 즉 l = 0, m = 1 이다.
# 그러면 while 0 <= 0 and 1 <= 1 의 조건을 돌게 되는데 2 가 1 보다 크기 때문에 else 조건에 걸려서 temp 에는 1이 들어가고 m 은 2가 되면서 while 문은 끝난다
# l = 0, m = 2, low = 0, mid = 0, high = 1이라 while l <= mid 조건을 돌게 된다. 이때 2가 temp 에 들어가고 l 이 1 증가하면서 while 문 끝난다
# while m <= high 는 m 이 이미 high 보다 크기 때문에 조건을 만족하지 않아서 실행되지 않는다
# temp = [1, 2] 이고 temp 의 순서대로 arr 을 수정해주면 arr = [1, 2, 4, 3] 이 된다
# 원래 arr 에서 앞의 두 원소는 정렬이 됐고 이제 뒤의 두 원소가 남았다
# 뒤의 두 원소도 위와 같은 방식으로 정렬이 돼서 arr = [1, 2, 3, 4] 가 된다
# 여기까지가 [2], [1], [4], [3] 의 정렬 과정이다

# 재귀적으로 가장 작은 원소 단위까지 나눈 부분이 정렬 된 것이라 그 상위의 [2, 1], [4, 3] 을 비교하는 작업을 수행해야 한다
# 이미 정렬이 끝났지만 재귀적으로 남은 부분이라 이 부분도 수행하고서 함수가 종료된다


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

    while l <= mid:
        temp.append(arr[l])
        l += 1

    while m <= high:
        temp.append(arr[m])
        m += 1

    t = 0
    while t < len(temp):
        arr[low + t] = temp[t]
        t += 1


arr = [2, 1, 4, 3]
merge_sort(0, len(arr) - 1)
print(arr)

# 참고
# https://www.daleseo.com/sort-merge/
