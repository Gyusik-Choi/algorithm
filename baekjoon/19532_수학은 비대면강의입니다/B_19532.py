def get_x_and_y():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            # if (a + d) * x + (b + e) * y == c + f:
            if a * x + b * y == c and d * x + e * y == f:
                return [x, y]


a, b, c, d, e, f = map(int, input().split())
answer = get_x_and_y()
print(answer[0], answer[1])
