def solution(price):
    if price >= 500000:
        return int(price * 0.8)

    if price >= 200000:
        return int(price * 0.9)

    if price >= 100000:
        return int(price * 0.95)

    return price


print(solution(150000))
print(solution(580000))
