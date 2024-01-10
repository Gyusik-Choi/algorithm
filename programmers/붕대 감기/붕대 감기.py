from unittest import TestCase
from collections import deque


def solution(bandage, health, attacks):
    max_health = health
    cast_time, recovery, plus_recovery = bandage
    attacks = deque(attacks)
    time = 0
    consecutive_success_time = 0

    while attacks:
        time += 1
        attack_time, attack_damage = attacks[0]

        if attack_time == time:
            if health - attack_damage <= 0:
                return -1

            health -= attack_damage
            attacks.popleft()
            consecutive_success_time = 0
            continue

        consecutive_success_time += 1
        health = min(health + recovery, max_health)

        if consecutive_success_time == cast_time:
            consecutive_success_time = 0
            health = min(health + plus_recovery, max_health)

    return health


class SolutionTest(TestCase):
    def test_solution(self):
        answer = solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
        self.assertEquals(answer, 5)

    def test_solution2(self):
        answer = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
        self.assertEquals(answer, -1)

    def test_solution3(self):
        answer = solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
        self.assertEquals(answer, -1)

    def test_solution4(self):
        answer = solution([1, 1, 1], 5, [[1, 2], [3, 2]])
        self.assertEquals(answer, 3)
