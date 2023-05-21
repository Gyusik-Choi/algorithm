from unittest import TestCase


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


class SelectionSortTest(TestCase):
    def test_selection_sort(self):
        arr = [2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted(arr), sorted_arr)
