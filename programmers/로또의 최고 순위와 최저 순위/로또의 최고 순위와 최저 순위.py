def solution(lotto, win_nums):
    zero_cnt = lotto.count(0)
    same_cnt = len([num for num in lotto if num in win_nums])
    highest = min(6, 7 - (zero_cnt + same_cnt))
    lowest = min(6, 7 - same_cnt)
    return [highest, lowest]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
