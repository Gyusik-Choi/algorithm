def three_sum(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 동일한 숫자 건너뛴다
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        # 투 포인터
        left, right = i + 1, len(nums) - 1

        while left < right:
            temp_sums = nums[i] + nums[left] + nums[right]

            if temp_sums > 0:
                right -= 1
                continue

            if temp_sums < 0:
                left += 1
                continue

            results.append([nums[i], nums[left], nums[right]])

            # 동일한 숫자 건너뛴다
            # 엄밀히 말하면 동일한 숫자가 여럿일 경우 마지막 동일한 숫자까지 간다
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            # 동일한 숫자 건너뛴다
            # 엄밀히 말하면 동일한 숫자가 여럿일 경우 마지막 동일한 숫자까지 간다
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            # 위 while 문으로 (동일한 숫자가 있을 경우) 마지막 동일한 숫자까지 왔고
            # 동일하지 않은 숫자로 넘어가기 위해 left 는 1을 더하고 right 는 1을 빼준다
            left, right = left + 1, right - 1

    return results


print(three_sum([-4, -1, -1, 0, 1, 2]))
