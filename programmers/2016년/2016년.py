def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_the_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    days = 0
    for i in range(a - 1):
        days += month[i]
    days += b - 1

    return day_of_the_week[days % 7]


print(solution(5, 24))

# 참고
# https://ittrue.tistory.com/460
