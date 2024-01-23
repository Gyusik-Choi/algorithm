from unittest import TestCase


def solution(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)

    # for 문을 빠져 나왔을 때
    # k 가 1 이상일 수 있음
    return ''.join(stack[:len(stack) - k])


class SolutionTest(TestCase):
    def test_solution(self):
        self.assertEqual("94", solution("1924", 2))

    def test_solution2(self):
        self.assertEqual("3234", solution("1231234", 3))

    def test_solution3(self):
        self.assertEqual("775841", solution("4177252841", 4))
