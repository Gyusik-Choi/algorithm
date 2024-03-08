def solution(n):
    arr = []

    def move(start, to):
        arr.append([start, to])

    def hanoi(num, start, via, to):
        if num == 1:
            move(start, to)
            return

        hanoi(num - 1, start, to, via)
        move(start, to)
        hanoi(num - 1, via, start, to)

    hanoi(n, 1, 2, 3)
    return arr


print(solution(2))

# 참고
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
