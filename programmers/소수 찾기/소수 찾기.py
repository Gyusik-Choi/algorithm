import math


def is_decimal(num):
    # 2부터 제곱근까지 나눴을 때 나머지가 없으면 소수 아니다
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def permutation(perms, temp, nums, length):
    if len(temp) == length:
        perms.append(temp[:])
        return

    for i in range(len(nums)):
        if not len(temp) and nums[i] == '0':
            continue

        # 중복 여부를 점검하기 쉽게 인덱스를 temp 에 넣는다
        # 예를 들어 문자열이 "011" 면
        # 1이 temp 에 있는지 여부로 중복 체크하면 안 된다
        # 1은 2개라서 중복으로 들어갈 수 있다
        # 2개 초과로 들어 가는지 봐야 하는데 이러면
        # 중복 여부를 판단하기 까다롭다
        # 인덱스를 temp 에 넣고 관리하면
        # 중복 여부를 판단하기 편리하다
        if i not in temp:
            temp.append(i)
            permutation(perms, temp, nums, length)
            temp.pop()

    return perms


def solution(numbers):
    permutations = []

    # 1부터 numbers 리스트 길이까지 순열을 구한다
    for i in range(1, len(numbers) + 1):
        permutations.append(permutation([], [], numbers, i))

    formatted_perms = []

    for perms in permutations:
        for perm in perms:
            formatted_perms.append(''.join(map(lambda x: numbers[x], perm)))

    cnt = 0

    for perm in set(formatted_perms):
        if int(perm) == 1:
            continue

        if is_decimal(int(perm)):
            cnt += 1

    return cnt


print(solution("17"))
print(solution("011"))

# 참고
# # https://stackoverflow.com/questions/13464152/typeerror-unhashable-type-list-when-using-built-in-set-function
