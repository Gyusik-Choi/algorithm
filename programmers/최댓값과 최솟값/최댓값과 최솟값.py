def solution(s):
    nums = sorted(list(map(int, s.split(" "))))
    return str(nums[0]) + " " + str(nums[-1])


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
