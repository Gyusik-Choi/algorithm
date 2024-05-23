from unittest import TestCase
import collections


class Solution:
    def min_window(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        #
        # enumerate(s, 1) 에서 1은
        # 시작 인덱스 값을 1로 한다는 의미다
        # 순회 자체는 0부터 하는데
        # 인덱스 0을
        # 0이 아닌 1로 right 에서 받겠다는 의미다
        for right, char in enumerate(s, 1):
            # bool 값이 1, 0 으로 대응해 뺄셈이 된다
            # need[char] 가 0보다 큰 경우만 True 가 되어 missing 에서 1을 뺀다
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            #
            # t 를 만족하는 집합은 구했고
            # left 와 right 사이의
            # 범위를 좁힐 수 있는지 확인한다
            if missing == 0:
                # need 의 value 가 음수인 key 는
                # t 에 포함되지 않는 문자다
                # left 의 범위를 오른쪽으로 이동해서
                # left 와 right 사이의 범위를 좁힌다
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # end 가 0인 경우는
                # start, end 가 아직 갱신되지 않은 상태다
                # start, end 의 초기값이 0이라
                # right - left 의 값이 더 클 수 있다
                # start, end 를 갱신하지 못하는 상황을
                # not end 조건으로 막는다
                if not end or right - left <= end - start:
                    start, end = left, right

                # 위의 while 문에서
                # need 의 값이 음수인 t 에 포함되지 않은 문자를
                # left 를 이동해서 건너 뛰었다
                #
                # 여기서는
                # 일단 left 를 한칸 이동하고
                # missing 을 1 더해서 0이 아닌 상태로 만든다
                # if 문을 빠져 나와서
                # missing 을 0으로 만들 right 를 찾는다
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_window(self):
        answer = self.solution.min_window("ADOBECODEBANC", "ABC")
        self.assertEqual(answer, "BANC")

    def test_min_window_2(self):
        answer = self.solution.min_window("a", "a")
        self.assertEqual(answer, "a")

    def test_min_window_3(self):
        answer = self.solution.min_window("a", "aa")
        self.assertEqual(answer, "")
