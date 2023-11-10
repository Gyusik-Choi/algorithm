def solution(numbers):
    nums = sorted(numbers)
    sum_nums = set()

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum_nums.add(nums[i] + nums[j])

    return sorted(list(sum_nums))


print(solution([0, 1, 2]))
print(solution([0, 0]))
