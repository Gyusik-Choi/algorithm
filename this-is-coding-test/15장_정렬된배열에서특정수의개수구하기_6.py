import unittest


def binary_search_right(lst, target):
    # 해당 코드는 python bisect 모듈의
    # bisect_right 함수를 참고해서 구현했다
    # bisect_right 함수는 찾는 숫자가 위치한
    # 마지막 인덱스 + 1 을 리턴한다
    # bisect_right 함수에 인자로 low, high 값을 선택적으로
    # 설정할 수 있는데 디폴트 high 값은 인자로 넘기는 리스트의 길이가 된다
    #
    # high 를
    # len(lst) - 1이 아닌
    # len(lst) 로 설정했다
    # high 를 len(lst) 로 설정해야
    # target 이 마지막 인덱스 까지 위치했을 경우
    # 마지막 인덱스 보다 1 큰 값이 리턴될 수 있다
    # len(lst) - 1 로 하게 되면
    # 리턴할 수 있는 최대 low 값이 배열의 마지막 인덱스가 된다
    # (리턴 하는 값은 low 다)
    #
    # 이때 문제가 될 수 있는 것은
    # [1, 2, 3] 에서 2를 찾는 값은 2가 되는데
    # [1, 2, 2] 에서 3을 찾는 값이 2가 된다
    # [1, 2, 3] 에서 2를 찾을 경우
    # 2가 위치한 1 인덱스 보다 1이 큰 2가 리턴 되는데
    # [1, 2, 2] 에서 3을 찾을 경우는
    # 원래 의도한 값은 3이 나와야 하지만
    # high 가 len(lst) - 1이라 low 가 최대로 커질 수 있는 값이
    # len(lst) - 1이라 2를 리턴한다
    #
    # 따라서 찾는 숫자가 위치한 마지막 인덱스 + 1이 나올 수 있도록
    # high 를 len(lst) 로 설정해야 한다
    #
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2

        if lst[mid] > target:
            high = mid
        else:
            low = mid + 1

    return low


def binary_search_left(lst, target):
    low, high = 0, len(lst)

    while low < high:
        mid = (low + high) // 2

        if lst[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return low


N, x = map(int, input().split())
numbers = list(map(int, input().split()))

left_idx = binary_search_left(numbers, x)
right_idx = binary_search_right(numbers, x)

cnt = right_idx - left_idx

if not cnt:
    print(-1)
else:
    print(cnt)

# 참고
# https://github.com/python/cpython/blob/3.11/Lib/bisect.py

class BinarySearchTest(unittest.TestCase):
    def test_binary_search_right(self):
        arr = [1, 1, 2, 2, 2, 2, 3, 3]
        num = 3
        idx = binary_search_right(arr, num)
        self.assertEqual(idx, 8)


if __name__ == '__main__':
    unittest.main()