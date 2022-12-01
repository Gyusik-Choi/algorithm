import unittest


def insertion_sort2(gap, idx, lst):
    for i in range(idx + gap, len(lst), gap):
        idx = i
        to_insert = lst[idx]

        while idx - gap >= 0 and lst[idx - gap] > to_insert:
            lst[idx] = lst[idx - gap]
            idx -= gap

        lst[idx] = to_insert


def insertion_sort(gap, idx, lst):
    for i in range(idx + gap, len(lst), gap):
        for j in range(i, -1, -gap):
            # 음수 인덱스 주의
            # 역순 탐색이 배열의 범위 안에 있으면 에러 발생 안 함
            if j - gap >= 0:
                if lst[j - gap] > lst[j]:
                    lst[j - gap], lst[j] = lst[j], lst[j - gap]
                else:
                    break


def get_gap(g) -> int:
    # 계속 1을 리턴해서
    # 무한 반복이 일어나지 않도록 하기 위함
    if g == 1:
        return 0

    gap = g // 2

    if not gap % 2:
        gap += 1

    return gap


def shell_sort(gap, lst):
    while gap > 0:
        for i in range(gap):
            insertion_sort(gap, i, lst)

        gap = get_gap(gap)


# arr = [10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16]
# shall_sort(get_gap(n), len(arr))
# print(arr)

# 참고
# https://gmlwjd9405.github.io/2018/05/08/algorithm-shell-sort.html


class ShallSortTest(unittest.TestCase):
    def test_shall_sort(self):
        lst = [10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16]
        length = len(lst)
        shell_sort(get_gap(length), lst)
        self.assertEqual(lst, [0, 1, 3, 4, 6, 8, 10, 15, 16, 20, 22])

    def test_shall_sort2(self):
        lst = [5, 4, 3, 2, 1]
        length = len(lst)
        shell_sort(get_gap(length), lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5])

    def test_shall_sort3(self):
        lst = [5, 4, 7, 1, 3, 6, 2]
        length = len(lst)
        shell_sort(get_gap(length), lst)
        self.assertEqual(lst, [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
