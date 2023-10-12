# 연립 방정식 가감법 활용
# https://mathbang.net/16#gsc.tab=0

def get_y():
    g = a * d
    h = b * d
    i = c * d

    j = d * a
    k = e * a
    l = f * a

    if g == j:
        return (i - l) // (h - k)

    return (i + l) // (h + k)


def get_x():
    g = a * e
    h = b * e
    i = c * e

    j = d * b
    k = e * b
    l = f * b

    # 여기서 착각한 부분이 있다
    # x 를 구하기 위해
    # 두 식의 y 계수를 똑같이 만들어 준다
    # 5x + y = 7
    # x - 3y = 11
    # 이 있을 때
    # 위의 식에 3을 곱하면
    # 5x + 3y = 21
    # x - 3y = 11
    # 이 된다
    # 이럴 때는 두 식을 더하면 된다
    # 위는 y 계수가 3, -3 이라 달라서
    # 더하면 되는데
    # 만약에 y 계수가 같으면
    # 더하면 안 되고 빼야 한다
    # 그래서 아래에 if 문으로 구분을 했는데
    # 실제로는 항상 if 문을 만족해서 그럴 필요가 없었다
    #
    # 왜냐하면
    # 5x + y = 7
    # x - 3y = 11
    # 이 입력에서
    # 5x + y = 7 에
    # 3을 곱하는게 아니라
    # -3을 곱하기 때문에
    # 계수가 같아진다
    #
    # 종이에 직접 써서 연립 방정식 풀이를 할 때는
    # 3을 곱해서 더하는 방식을 사용 했다보니
    # 코드 상에서 이런 방식을 떠올리게 되면서 착각을 했다
    #
    # 그러나 코드는
    # 서로의 계수를 음수 양수 상관없이
    # 그대로 곱하므로 항상 같아진다

    if h == k:
        # return i - l // g - j
        # 위 코드는 나눗셈이 먼저 실행 되므로 주의해야 한다
        return (i - l) // (g - j)

    return (i + l) // (g + j)


def get_x_and_y():
    return [get_x(), get_y()]


a, b, c, d, e, f = map(int, input().split())
print(*get_x_and_y())
# 1 3 -1 4 1 7
