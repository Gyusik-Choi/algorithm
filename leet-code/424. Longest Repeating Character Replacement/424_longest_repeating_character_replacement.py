from collections import Counter
from unittest import TestCase


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_cnt = Counter()
        for right in range(len(s)):
            char_cnt[s[right]] += 1
            if right - left - char_cnt.most_common(1)[0][1] + 1 > k:
                char_cnt[s[left]] -= 1
                left += 1
                continue
            max_len = max(max_len, right - left + 1)
        return max_len


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_character_replacement(self):
        answer = self.solution.character_replacement("ABAB", 2)
        self.assertEqual(answer, 4)

    def test_character_replacement_2(self):
        answer = self.solution.character_replacement("AABABBA", 1)
        self.assertEqual(answer, 4)

# AAAAABBBCBBB
