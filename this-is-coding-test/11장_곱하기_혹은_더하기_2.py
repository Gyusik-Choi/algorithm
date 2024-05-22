import unittest


def get_sums(s):
    sums = s[0]

    for i in range(1, len(s)):
        num = s[i]

        if sums > 1 and num > 1:
            sums *= s[i]
            continue

        sums += num

    return sums


S = list(map(int, input()))
print(get_sums(S))


class UnitTest(unittest.TestCase):
    def test_get_sums(self):
        s = [0, 0, 1, 0, 1]
        self.assertEqual(get_sums(s), 2)

    def test_get_sums_2(self):
        s = [1, 2, 3, 4, 5, 1]
        self.assertEqual(get_sums(s), 181)
