def solution(array, height):
    return len(list(filter(lambda x: x > height, array)))


print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))
