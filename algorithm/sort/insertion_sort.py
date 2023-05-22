from unittest import TestCase


# 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr

# 삽입 정렬 개선
def insertion_sort2(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] < arr[j]:
                break
            else:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr

# 삽입 정렬 개선 2
def insertion_sort3(arr):
    for idx in range(1, len(arr)):
        i = idx
        to_insert = arr[idx]
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert

    return arr


class InsertionSortTest(TestCase):
    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]),
            sorted([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7])
        )

    def test_insertion_sort2(self):
        self.assertEqual(
            insertion_sort2([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]),
            sorted([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7])
        )

    def test_insertion_sort3(self):
        self.assertEqual(
            insertion_sort3([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7]),
            sorted([2, 3, 4, 1, 1, 5, 5, 3, 4, 6, 8, 9, 7])
        )
