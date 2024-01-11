from unittest import TestCase


# 서로 선물 주고받은 기록 -> 이차원 딕셔너리
# 서로 간의 선물 지수 비교 -> 일차원 딕셔너리
def solution(friends, gifts):
    gift_history = {f: {fr: 0 for fr in friends if f != fr} for f in friends}
    gift_index = {f: 0 for f in friends}

    for g in gifts:
        a, b = g.split()
        gift_history[a][b] += 1
        gift_index[a] += 1
        gift_index[b] -= 1

    friend_list = sorted(list(gift_index))
    new_gift = {f: 0 for f in friends}

    for i in range(len(friend_list) - 1):
        a = friend_list[i]

        for j in range(i + 1, len(friend_list)):
            b = friend_list[j]

            a_history = gift_history[a][b]
            b_history = gift_history[b][a]
            a_index = gift_index[a]
            b_index = gift_index[b]

            if a_history == b_history:
                # a_index 와 b_index 가 같은 경우는 제외
                if a_index > b_index:
                    new_gift[a] += 1
                elif a_index < b_index:
                    new_gift[b] += 1
            else:
                if a_history > b_history:
                    new_gift[a] += 1
                else:
                    new_gift[b] += 1

    return list(map(lambda x: x[1], sorted(new_gift.items(), key=lambda x: -x[1])))[0]


class TestSolution(TestCase):
    def test_solution(self):
        answer = solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
        self.assertEqual(answer, 2)

    def test_solution2(self):
        answer = solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
        self.assertEqual(answer, 4)

    def test_solution3(self):
        answer = solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])
        self.assertEqual(answer, 0)
