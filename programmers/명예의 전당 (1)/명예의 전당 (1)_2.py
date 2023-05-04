import heapq


def solution(k, score):
    hall_of_fame = []
    lowest_points_from_hall_of_fame = []

    for idx, s in enumerate(score):
        heapq.heappush(hall_of_fame, s)

        if len(hall_of_fame) > k:
            # heapq.heappop(hall_of_fame)
            hall_of_fame.pop(0)

        lowest_points_from_hall_of_fame.append(hall_of_fame[0])

    return lowest_points_from_hall_of_fame


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
