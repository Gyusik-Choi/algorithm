import math


def prime_num_check(num, square):
    for j in range(2, int(square) + 1):
        if num % j == 0:
            return 0
    else:
        return 1


lst = ['2']
for i in range(3, 10 ** 6 + 1):
    square_root = math.sqrt(i)
    check = prime_num_check(i, square_root)
    if check:
        lst.append(str(i))

print(' '.join(lst))
