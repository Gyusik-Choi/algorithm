# bisect 모듈의
# bisect_left 메소드를 참고해서 구현했다
# bisect_left 메소드는 찾는 숫자가 여러개일 경우 가장 첫번째 인덱스를 리턴한다
#
# bisect_left 메소드에서 주의할 점은 찾는 숫자가 없는 경우도 값을 리턴하고
# 리턴 값이 리스트의 길이를 넘어갈 수도 있어서 주의해야 한다
#
# 소스코드를 보면 lo, hi 변수를 이용해
# while 문으로 이진 탐색을 하는데 hi 변수의 값이 리스트의 길이로 되어있다
# 만약에 찾는 값이 리스트에 있는 최대값 보다 더 큰 경우 리스트의 길이를 리턴한다
# 이 값으로 리스트를 조회하면 잘못된 인덱스로 에러가 발생한다
#
# 리턴 값이 리스트에서 조회할 수 있는 인덱스 범위를 벗어 났는지 검사하고
# 인덱스 범위를 벗어나지 않았다면 해당 인덱스 값이 실제로 찾는 값과 일치 하는지 확인해야 한다
def binary_search(arr, num):
    # bisect 모듈의
    # bisect_left 메소드와 달리
    # high 에
    # arr 의 길이가 아닌
    # arr 의 길이 - 1 을 할당
    #
    # low 가 가질 수 있는 최대 값이
    # arr 의 길이 - 1 이 되므로
    # low 가 arr 의 인덱스 범위를 벗어나지 않는다
    # low 로 인덱스 조회를 하더라도 인덱스 에러가 발생하지 않는다
    # 그래도 찾는 값이 없는 경우도 값을 리턴하기 때문에
    # low 값이 찾는 값과 일치 하는지
    # 해당 함수를 호출한 쪽에서 확인해야 한다
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < num:
            low = mid + 1
        else:
            # high 에
            # mid - 1 이 아니라
            # mid 를 할당한다
            #
            # arr -> [1, 1, 2, 2, 2, 4, 5, 5]
            # num -> 3
            # 위의 경우
            # 3 은 없고 3 보다 크거나 작은 숫자만 있다
            # high 에 mid - 1 을 할당 했다면
            # 리턴 값은 3 보다 작은 2 를 가리키는 4 다
            # high 에 mid - 1 을 해서
            # 리턴 값은 3 보다 큰 4 를 가리키는 5 다
            high = mid

    return low

# 참고
# https://github.com/python/cpython/blob/v3.9.0/Lib/bisect.py
