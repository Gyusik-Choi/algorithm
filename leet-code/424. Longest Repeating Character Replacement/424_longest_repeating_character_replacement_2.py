from collections import Counter
from unittest import TestCase


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        left = right = 0
        # defaultdict 대신 Counter 를 사용한 이유는
        # 아래의 most_common 메소드를 사용하기 위해서다
        char_cnt = Counter()
        for right in range(len(s)):
            char_cnt[s[right]] += 1
            # 첫번째 풀이의 if 문을 여기서 살짝 바꿨다
            #
            # left 부터 right 까지의 범위를
            # 한 문자로 채울 수 없는 경우
            # (left 부터 right 까지의 범위를
            # 가장 많이 나온 문자와 k 를 합친 값으로 커버할 수 없는 경우)
            # (가장 많이 나온 문자와 다른 문자를 k번 만큼
            # 가장 많이 나온 문자로 바꿀 수 있어서 가장 많이 나온 문자 하나로
            # left 부터 right 를 채울 수 있는지 판단한다)
            if right - left + 1 > char_cnt.most_common(1)[0][1] + k:
                char_cnt[s[left]] -= 1
                left += 1
        # right 와 left 둘 다 0부터 시작해서
        # right 와 left 가 같을 때 right 에서 left 를 빼면 0이 된다
        # right 와 left 가 같을 때 문자 하나를 나타내서 1이 되야 한다
        #
        # 최대 길이를 별도의 변수로 따로 구하지 않았다
        # 최대 길이가 구해진 상태에서
        # 최대 길이를 더 이상 갱신할 수 없으면
        # right 가 증가할때 left 도 함께 증가한다
        #
        # 한 문자로 left 부터 right 를 채울 수 있어서
        # if 문을 충족하지 않으면 right 만 커지고 left 는 커지지 않는다
        # 그러다 한 문자로 left 부터 right 를 채울 수 없으면
        # right 와 함께 left 도 커지면서 right 와 left 의 범위가 유지된다
        #
        # 그러면 만약에 첫 부분이 최대 길이인줄 알았으나
        # 나중에 진짜 최대 길이가 나오면 값을 제대로 구할 수 있는지 궁금했다
        # 예를 들어
        # s -> AAABACDEFGGGGHG, k -> 1 인 경우
        # 최대 길이에 해당하는 구간은
        # 앞의 AAABA 구간이 아닌 맨 뒤의 GGGGHG 구간이다
        # 이때 AAABA 까지 right 만 증가하다가
        # C 부터 left 도 증가한다
        # 이는 H까지 지속되다 마지막 G 에 와서 멈춘다
        # 마지막 G 에서 left 가 증가하지 않으면서
        # 최대 길이를 구할 수 있다
        return right - left + 1


class SolutionTest(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_character_replacement(self):
        answer = self.solution.character_replacement("ABAB", 2)
        self.assertEqual(answer, 4)

    def test_character_replacement_2(self):
        answer = self.solution.character_replacement("AABABBA", 1)
        self.assertEqual(answer, 4)

# "AAABACDEFGGGGHG"