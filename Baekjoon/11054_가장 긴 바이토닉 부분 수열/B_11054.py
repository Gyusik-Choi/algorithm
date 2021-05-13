def lis(nums):
    dp_lis = [1] * len(nums)
    if len(nums) > 1:
        for i in range(1, len(nums)):
            target = nums[i]
            for j in range(i - 1, -1, -1):
                if target > nums[j]:
                    dp_lis[i] = max(dp_lis[i], dp_lis[j] + 1)
    return dp_lis


def lds(nums):
    dp_lds = [1] * len(nums)
    if len(nums) > 1:
        for i in range(len(nums) - 2, -1, -1):
            target = nums[i]
            for j in range(i + 1, len(nums)):
                if target > nums[j]:
                    dp_lds[i] = max(dp_lds[i], dp_lds[j] + 1)
    return dp_lds


N = int(input())
numbers = list(map(int, input().split()))

lis_dp = lis(numbers)
lds_dp = lds(numbers)

max_length = 1
for k in range(len(numbers)):
    sums = lis_dp[k] + lds_dp[k] - 1
    if max_length < sums:
        max_length = sums
print(max_length)

# 참고
# https://st-lab.tistory.com/136?category=868019
# https://www.acmicpc.net/board/view/63004 (lds 부분 구하는 함수에서 반복문을 마지막 요소까지 구하지 않았던 부분을 해결)
