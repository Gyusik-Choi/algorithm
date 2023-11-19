from collections import defaultdict


def solution(nums):
    labs = defaultdict(int)

    for num in nums:
        labs[num] += 1

    # 리스트 절반 길이 보다 키의 갯수가 더 크면 리스트 절반 길이 리턴
    # 리스트 절반 길이 보다 키의 갯수가 더 작으면 키의 갯수 리턴
    # => 둘 중 더 작은 값을 리턴
    return min(len(labs.keys()), len(nums) // 2)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
