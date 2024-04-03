# '파이썬 알고리즘 인터뷰' 에 수록된
# LeetCode 75번 Sort Colors 를 학습 하면서 알게된
# Dutch National Flag Problem 을
# 정리하기 위해 작성한다

# !
# 이 정렬은
# 리스트에 0, 1, 2 만 있는 경우에 적용할 수 있다
# 이 외의 정수가 있다면 올바르게 정렬할 수 없다
# !
from unittest import TestCase


def dnf_sort(nums: list[int]) -> list[int]:
    r, w, b = 0, 0, len(nums) - 1

    while w <= b:
        if nums[w] < 1:
            nums[r], nums[w] = nums[w], nums[r]
            r += 1
            w += 1
        elif nums[w] > 1:
            nums[w], nums[b] = nums[b], nums[w]
            b -= 1
        else:
            w += 1

    return nums


class DnfSortTest(TestCase):
    def test_dnf_sort(self):
        arr = [2, 1, 0]
        dnf_sort(arr)
        self.assertEqual([0, 1, 2], arr)

    def test_dnf_sort2(self):
        arr = [2, 2, 0, 1, 2]
        dnf_sort(arr)
        self.assertEqual([0, 1, 2, 2, 2], arr)

    # 0, 1, 2이외에 -1, 3이 있어서 제대로 정렬되지 않는다
    def test_dnf_sort3(self):
        arr = [-1, 2, 2, 0, 1, 2, 3]
        dnf_sort(arr)
        self.assertNotEqual([-1, 0, 1, 2, 2, 2, 3], arr)

# 참고
# 파이썬 알고리즘 인터뷰
# https://leetcode.com/problems/sort-colors/description/
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
