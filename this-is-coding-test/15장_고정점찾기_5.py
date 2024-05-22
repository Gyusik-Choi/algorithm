def binary_search(lst):
    # '정렬된 배열에서 특정 수의 개수 구하기' 에서 구현한
    # binary_search_left, binary_search_right 함수와 달리
    # high 를 len(lst) 가 아닌 len(lst) - 1 로 설정했다
    # while 문을 돌고 나올 수 있는 low 값의 범위를
    # 0 에서 len(lst) - 1 로 제한해서
    # low 가 0이나 len(lst) - 1 이 나왔을 경우
    # 고정점이 없어서 해당 값이 나올 수 있기 때문에 별도로 검증을 한다
    # len(lst) - 1 로 해서 얻는 또 다른 장점은 고정점 검증시 코드가 간결해 진다
    # 바로 low 값으로 lst 에 인덱스 접근이 가능하다
    # 만약 high 를 len(lst) 로 했다면 low 가 len(lst) 가 나올 수 있기 때문에
    # 바로 인덱스 접근을 할 수 없어서 low 가 0인 경우와 len(lst) 인 경우를 따로 코드 작성을 해야 한다
    low, high = 0, len(lst) - 1

    while low < high:
        mid = (low + high) // 2

        if lst[mid] == mid:
            low = mid
            break

        if lst[mid] > mid:
            high = mid
        else:
            low = mid + 1

    # low 가 0 혹은 len(lst) - 1 인 경우
    # 고정점이 없어서 해당 값이 나왔을 수 있기 때문에
    # 고정점이 맞는지 검증한다
    if lst[low] != low:
        return -1

    return low


N = int(input())
numbers = list(map(int, input().split()))
num = binary_search(numbers)
print(num)
