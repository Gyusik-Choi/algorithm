from unittest import TestCase


# 거품정렬
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 거품정렬 개선
def bubble_sort2(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

# 거품정렬 추가 개선
def bubble_sort3(arr):
    idx = len(arr) - 1

    while idx > 0:
        last_changed = 0

        for i in range(idx):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_changed = i

        idx = last_changed

    return arr


class BubbleSortTest(TestCase):
    def test_bubble_sort(self):
        arr = [4, 6, 1, 7, 3, 5, 2]
        sorted_arr = bubble_sort(arr)
        self.assertEqual(sorted(arr), sorted_arr)

    def test_bubble_sort2(self):
        arr = [4, 6, 1, 7, 3, 5, 2]
        sorted_arr = bubble_sort2(arr)
        self.assertEqual(sorted(arr), sorted_arr)

    def test_bubble_sort3(self):
        arr = [4, 6, 1, 7, 3, 5, 2]
        sorted_arr = bubble_sort3(arr)
        self.assertEqual(sorted(arr), sorted_arr)

# 참고
# https://www.daleseo.com/sort-bubble/
