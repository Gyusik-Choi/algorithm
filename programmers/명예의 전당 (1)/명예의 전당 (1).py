def solution(k, score):
    hall_of_fame = []
    lowest_points_from_hall_of_fame = []

    for idx, s in enumerate(score):
        hall_of_fame.append(s)
        hall_of_fame.sort(reverse=True)

        if len(hall_of_fame) > k:
            hall_of_fame.pop()

        lowest_points_from_hall_of_fame.append(hall_of_fame[-1])

    return lowest_points_from_hall_of_fame


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
