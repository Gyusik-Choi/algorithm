from unittest import TestCase
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        cnt = 0
        majority = -10 ** 9 - 1
        for num in nums:
            if not cnt:
                cnt += 1
                majority = num
            elif majority == num:
                cnt += 1
            else:
                cnt -= 1
        return majority


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_majority_element(self):
        answer = self.solution.majority_element([3, 2, 3])
        self.assertEqual(3, answer)

    def test_majority_element_2(self):
        answer = self.solution.majority_element([2, 2, 1, 1, 1, 2, 2])
        self.assertEqual(2, answer)

    def test_majority_element_3(self):
        answer = self.solution.majority_element([2, 3, 2, 1, 2, 1, 2])
        self.assertEqual(2, answer)

# 참고
# https://doozi0316.tistory.com/entry/leetCode-169-Majority-Element-Easy-%ED%92%80%EC%9D%B4
# https://kkminseok.github.io/posts/leetcode_Major_Element/
