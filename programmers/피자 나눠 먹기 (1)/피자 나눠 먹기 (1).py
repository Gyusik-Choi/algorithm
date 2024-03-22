def solution(n):
    cnt = n // 7
    left = n % 7
    if left:
        cnt += 1
    return cnt
