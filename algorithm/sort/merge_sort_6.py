from unittest import TestCase


def merge_sort(arr):
    def sort(low, high):
        if low >= high:
            return

        mid = (low + high) // 2
        sort(low, mid)
        sort(mid + 1, high)

        l = low
        m = mid + 1
        temp = []
        while l <= mid and m <= high:
            if arr[l] < arr[m]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[m])
                m += 1

        while l <= mid:
            temp.append(arr[l])
            l += 1

        while m <= high:
            temp.append(arr[m])
            m += 1

        t = 0
        while t < len(temp):
            arr[low + t] = temp[t]
            t += 1

    sort(0, len(arr))
    return arr


# arr = [2, 1, 4, 3]
# merge_sort(0, len(arr) - 1)
# print(arr)

# 참고
# https://www.daleseo.com/sort-merge/

class MergeSortTest(TestCase):
    def test_merge_sort(self):
        lst = [2, 1, 4, 3]
        self.assertEquals(merge_sort(lst), [1, 2, 3, 4])

