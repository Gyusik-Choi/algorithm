import math


def is_prime_number(num):
    square_root = int(math.sqrt(num))

    for n in range(2, square_root + 1):
        if num % n == 0:
            return False

    return True


def get_combination(nums, limit):
    combinations = []

    def dfs(idx, temp):
        if len(temp) == limit:
            combinations.append(temp[:])
            return

        for i in range(idx, len(nums)):
            temp.append(nums[i])
            dfs(i + 1, temp)
            temp.pop()

    dfs(0, [])
    return combinations


def solution(nums):
    combs = get_combination(nums, 3)
    cnt = 0

    for comb in combs:
        if is_prime_number(sum(comb)):
            cnt += 1

    return cnt


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
