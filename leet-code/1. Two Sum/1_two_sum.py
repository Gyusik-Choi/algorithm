def two_sum(nums, target):
    dic = dict()

    for idx, num in enumerate(nums):
        dic[num] = idx

    for idx, num in enumerate(nums):
        # if target - num in nums and idx != dic[target - num]:
        # 위처럼 list 에 target - num 이 있는지 조회하는 것 보다
        # 아래처럼 dictionary 에 target - num 이 있는지 조회하는게 훨씬 빠르다
        if target - num in dic and idx != dic[target - num]:
            return [idx, dic[target - num]]


print(two_sum([2, 7, 11, 15], 9))
