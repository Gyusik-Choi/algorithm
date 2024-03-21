from unittest import TestCase


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
        # pivot 이 아닌 arr[high] 로 한 이유는
        # 위의 for 문에 의해 high 인덱스 값이
        # pivot 이 아닌 다른 값으로 바뀔 수 있다
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
