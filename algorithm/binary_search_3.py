from unittest import TestCase


def binary_search(arr, num):
    low, high = 0, len(arr) - 1

    # 마지막 인덱스까지 확인을 하려면
    # low <= high 범위로 설정해야 한다
    #
    # arr -> [1, 2, 3, 4, 5, 6, 7]
    # num -> 1
    # 위처럼 arr 의 가장 첫번째 값을 찾는 경우
    # high 를 mid - 1 로 계속 줄이다
    # low -> 0, high -> 3, mid -> 1 인 상황이 끝나면
    # high 를 mid - 1 로 해서
    # low 와 high 가 같아지는데
    # 만약에 while low < high 였다면
    # while 문이 종료돼서 원하는 값을 찾을 수 없다
    # while low <= high 조건이어야 1을 찾을 수 있다
    #
    # arr -> [1, 2, 3, 4, 5, 6, 7]
    # num -> 7
    # 위처럼 arr 의 맨 마지막 값을 찾는 경우도 마찬가지다
    # low 를 mid + 1 로 계속 늘리다
    # low -> 4, high -> 6, mid -> 5 인 상황이 끝나면
    # low 를 mid + 1 로 해서
    # low 와 high 가 같아지는데
    # 만약에 while low < high 였다면
    # while 문이 종료돼서 원하는 값을 찾을 수 없다
    # while low <= high 조건이어야 7을 찾을 수 있다
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == num:
            return mid

        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("can't find num in arr")


class BinarySearchTest(TestCase):
    def test_binary_search(self):
        answer = binary_search([1, 2, 3, 4, 5, 6, 7], 1)
        self.assertEqual(answer, 0)

    def test_binary_search_2(self):
        answer = binary_search_2([1, 2, 3, 4, 5, 6, 7], 1)
        self.assertEqual(answer, 0)

# 참고
# 파이썬 알고리즘 인터뷰
