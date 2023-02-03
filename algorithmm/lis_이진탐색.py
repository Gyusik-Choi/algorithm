def binary_search(start, end, target):
    if start < end:
        mid = (start + end) // 2
        # lis[mid] 가 target 보다 큰 경우
        # mid 보다 작은 범위를 탐색해야한다
        if lis[mid] > target:
            # mid - 1이 0이상이어야 mid - 1을 할 수가 있다. mid - 1이 음수면 인덱스가 벗어남.
            if mid - 1 > -1:
                if lis[mid - 1] < target:
                    return mid
                return binary_search(start, mid - 1, target)
            # mid 가 0인 경우
            # mid - 1이 0보다 작으면 mid - 1이 아니라 mid 를 넣어준다 (mid 가 0보다 작아질 수는 없다)
            else:
                return binary_search(start, mid, target)
        # lis[mid] 가 target 과 같은 경우
        # mid 를 리턴한다(lis 에 변화없음)
        elif lis[mid] == target:
            return mid
        # lis[mid] 가 target 보다 작은 경우
        else:
            # lis[mid + 1] 이 target 보다 크다면 target 은 lis[mid] 와 lis[mid + 1] 사이에 있기 때문에
            # mid + 1을 리턴하여 lis[mid + 1]을 target 값으로 교체
            if lis[mid + 1] > target:
                return mid + 1
            # lis[mid + 1] 마저 target 보다 작으면 mid + 1과 end 사이의 값을 탐색해야 한다.
            return binary_search(mid + 1, end, target)
    return end


numbers = [10, 20, 30, 10, 30, 40, 20, 50, 60, 20]
lis = [numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i] > lis[-1]:
        lis.append(numbers[i])
    else:
        # numbers[i] 와 lis[-1] 이 같은 경우는 제외
        if numbers[i] < lis[-1]:
            binary_search(0, len(lis) - 1, numbers[i])

print(lis)
