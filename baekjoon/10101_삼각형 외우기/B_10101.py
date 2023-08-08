def is_same_two_angles(angles: list) -> bool:
    return len(list(set(angles))) == 2


def check_angles(a1: int, a2: int, a3: int) -> str:
    if a1 == a2 == a3 == 60:
        return 'Equilateral'

    if a1 + a2 + a3 == 180 and is_same_two_angles([a1, a2, a3]):
        return 'Isosceles'

    if a1 + a2 + a3 == 180:
        return 'Scalene'

    return 'Error'


angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
print(check_angles(angle1, angle2, angle3))
