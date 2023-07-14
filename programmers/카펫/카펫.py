def get_brown(yellow_y, yellow_x):
    return (yellow_y + 2) * 2 + (yellow_x * 2)


def solution(brown, yellow):
    # 한 줄, 두 줄, 세 줄
    # 가로가 더 길 때까지
    y_y = 1
    y_x = yellow

    while True:
        if get_brown(y_y, y_x) == brown:
            print(y_y, y_x)
            return [y_x + 2, y_y + 2]

        y_y += 1

        while yellow % y_y:
            y_y += 1

        y_x = yellow // y_y


print(solution(28, 36))
print(solution(14, 4))
print(solution(12, 4))
