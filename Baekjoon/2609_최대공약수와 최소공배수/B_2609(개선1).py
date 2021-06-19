first_num, second_num = map(int, input().split())
divisor = 1
while True:
    flag = False
    smaller_num = min(first_num, second_num)
    if first_num == 1 or second_num == 1:
        break
    else:
        for i in range(2, smaller_num + 1):
            if first_num % i == 0 and second_num % i == 0:
                first_num //= i
                second_num //= i
                divisor *= i
                flag = True
                break
    if not flag:
        break

print(divisor * 1)
print(divisor * first_num * second_num)