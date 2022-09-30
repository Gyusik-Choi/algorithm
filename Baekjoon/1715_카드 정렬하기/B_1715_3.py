import heapq
import sys


def get_compare_count(cards):
    answer = 0

    while len(cards) > 1:
        sums = 0
        sums += heapq.heappop(cards)
        sums += heapq.heappop(cards)

        heapq.heappush(cards, sums)
        answer += sums

    return answer


N = int(sys.stdin.readline())
card_heap = []

for _ in range(N):
    c = int(sys.stdin.readline())
    heapq.heappush(card_heap, c)

print(get_compare_count(card_heap))

# 반례
# https://www.acmicpc.net/board/view/72799

# 4
# 30
# 40
# 50
# 100
# => 410

# 4
# 30
# 40
# 50
# 60
# => 360

# 8
# 30
# 40
# 50
# 20
# 10
# 100
# 60
# 120
# => 1160

# 8
# 30
# 40
# 50
# 20
# 10
# 100
# 60
# 10
# => 860

# 4
# 120
# 40
# 100
# 20
# => 500
