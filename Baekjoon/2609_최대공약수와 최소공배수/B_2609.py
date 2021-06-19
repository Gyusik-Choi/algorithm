first_num, second_num = map(int, input().split())
if first_num == 1 or second_num == 1:
    print(1)
    print(first_num * second_num)
else:
    first, second = first_num, second_num
    divisor = 1
    while True:
        flag = False
        smaller_num = min(first, second)
        for j in range(2, smaller_num + 1):
            if first % j == 0 and second % j == 0:
                divisor *= j
                first //= j
                second //= j
                smaller_num = min(first, second)
                flag = True
                break
        if not flag:
            break
    print(divisor)
    print(divisor * first * second)
