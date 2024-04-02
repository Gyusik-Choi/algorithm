from unittest import TestCase


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram(self):
        result = self.solution.is_anagram("anagram", "nagaram")
        self.assertEqual(True, result)

    def test_is_anagram2(self):
        result = self.solution.is_anagram("rat", "car")
        self.assertEqual(False, result)
