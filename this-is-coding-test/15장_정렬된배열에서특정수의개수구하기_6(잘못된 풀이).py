# number[mid] >= x 일때 high = mid 인지
# numbers[mid] > x 일때 high = mid 인지에 따라서
# 결과 값이 다르다
#
# numbers[mid] >= x 일때 high = mid 이면
# 찾는 대상의 시작 인덱스 구한다
# number[mid] > x 일때 high = mid 이면
# 찾는 대상 보다 큰 숫자를 찾게 되므로 바로 다음 인덱스 구한다
#
# 참고
# https://github.com/python/cpython/blob/3.11/Lib/bisect.py

def binary_search_right(low, high, target):
    while low < high:
        mid = (low + high) // 2

        if numbers[mid] > target:
            high = mid
        else:
            low = mid + 1

    return low

def binary_search_left(low, high, target):
    while low < high:
        mid = (low + high) // 2

        if numbers[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return low


N, x = map(int, input().split())
numbers = list(map(int, input().split()))

lower_x = binary_search_left(0, N - 1, x)
higher_x = binary_search_right(0, N - 1, x)

cnt = higher_x - lower_x

if not cnt:
    print(-1)
else:
    print(cnt)

# 반례
# 8 3
# 1 1 2 2 2 2 3 3
# => 2가 나와야 하는데 1이 나온다
# 원인은 bisect 모듈과 다르게
# high 의 길이를 len(numbers) - 1 로 잡았다
# bisect 모듈로 풀이를 하게 되면
# bisect 모듈의 디폴트 high 값은 len(numbers) 가 된다
