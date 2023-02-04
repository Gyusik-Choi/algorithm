import unittest


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]

    while low <= high:
        while arr[low] < pivot:
            low += 1

        while arr[high] > pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    return low


def sort(arr, low, high):
    if high <= low:
        return

    mid = partition(arr, low, high)

    sort(arr, low, mid - 1)
    sort(arr, mid, high)

    return arr


def quick_sort(arr):
    return sort(arr, 0, len(arr) - 1)


class QuickSortTest(unittest.TestCase):
    def test_quick_sort(self):
        lst = [5, 1, 4, 3, 2]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, sorted(lst))

    def test_quick_sort_2(self):
        lst = [5, 1, 4, 3, 2, 7, 6, 9, 8]
        sorted_lst = quick_sort(lst)
        self.assertEqual(sorted_lst, sorted(lst))

# 참고
# https://www.daleseo.com/sort-quick/
