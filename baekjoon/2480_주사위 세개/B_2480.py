def get_same_dice():
    if first == second or first == third:
        return first

    if second == third:
        return second


def is_all_different_dice():
    if first != second and first != third and second != third:
        return True

    return False


first, second, third = list(map(int, input().split()))

# 같은 눈 3개
if first == second == third:
    print(10000 + first * 1000)
# 모두 다른 눈
elif is_all_different_dice():
    print(max(first, second, third) * 100)
# 같은 눈 2개
else:
    print(1000 + get_same_dice() * 100)

# 주의할 점은
# first != second != third
# 위의 조건은 first 와 third 가 같은 경우를
# 걸러낼 수 없다
