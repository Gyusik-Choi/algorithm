from unittest import TestCase
# 퀵 정렬은 불안정 정렬
# 불안정 정렬이란
# 기존의 정렬했던 순서가
# 다른 기준으로 재정렬 하면서 깨지는 정렬
# 예를 들면 [3, 5, 5] 를 아래의 코드로
# 퀵 정렬하면
# partition 함수 안에서
# left 는 1이 되고
# high 는 2라서 둘 다 5지만
# swap 이 일어난다
# 만약에 숫자 외에 시간 정보가 있어서
# 시간 순서로 정렬이 되어 있는데
# 숫자를 기준으로 다시 정렬을 하는 경우라면
# 시간 순서가 이때 깨진다


# 로무토 파티션 기반 퀵 정렬
def quick_sort(arr):
    def sort(low, high):
        if low < high:
            pivot = partition(low, high)
            # pivot 좌측 정렬
            # pivot 의 좌측은 pivot 의 값 보다 작은 값들만 있다
            sort(low, pivot - 1)
            # pivot 우측 정렬
            # pivot 의 우측은 pivot 의 값 보다 큰 값들만 있다
            sort(pivot + 1, high)
        return arr

    def partition(low, high):
        # 맨 우측의 값을 피벗으로 설정
        pivot = arr[high]
        left = low
        for right in range(low, high):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        # pivot 은 리스트를 참조 하는게 아니라 정수 값을 갖는다
        # arr[high] 가 아니라 pivot 을 쓴다면
        # arr[left] 와 pivot 변수의 값이 바뀌는 것이다
        # high 인덱스의 값에는 영향을 줄 수 없다
        # high 인덱스의 값을 바꾸기 위해
        # pivot 이 아니라 arr[high] 로 했다
        arr[left], arr[high] = arr[high], arr[left]
        return left

    return sort(0, len(arr) - 1)


class QuickSortTest(TestCase):
    def test_quick_sort(self):
        arr = [2, 8, 7, 1, 3, 5, 6, 4]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, sorted(arr))

# 참고
# 파이썬 알고리즘 인터뷰
# https://riverblue.tistory.com/39
