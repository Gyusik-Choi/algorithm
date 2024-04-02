from collections import defaultdict
from unittest import TestCase


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        dic_s = defaultdict(int)
        for char in s:
            dic_s[char] += 1

        dic_t = defaultdict(int)
        for char in t:
            dic_t[char] += 1

        for k, v in dic_t.items():
            if k not in dic_s:
                return False

            if v != dic_s[k]:
                return False

        # dic_s 에는 존재하는 키인데
        # dic_t 에는 존재하지 않는 경우
        if len(dic_s.keys()) != len(dic_t.keys()):
            return False
        return True


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram(self):
        result = self.solution.is_anagram("anagram", "nagaram")
        self.assertEqual(True, result)

    def test_is_anagram2(self):
        result = self.solution.is_anagram("rat", "car")
        self.assertEqual(False, result)

    # LeetCode 에 제출시 실패했던 테스트 케이스
    # dic_s 에는 존재하는 키인데
    # dic_t 에는 존재하지 않는 경우를
    # 고려하지 않아서 오답이 나왔음
    def test_is_anagram3(self):
        result = self.solution.is_anagram("ab", "a")
        self.assertEqual(False, result)
