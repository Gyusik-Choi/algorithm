def solution(n):
    for num in range(1, n):
        if n % num == 1:
            return num
