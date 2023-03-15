n = int(input())

numbers = [0] * n
numbers[0] = 1

i2 = 0
i3 = 0
i5 = 0

num2 = 2
num3 = 3
num5 = 5

num2_acc = 2
num3_acc = 3
num5_acc = 5

for i in range(1, n):
    numbers[i] = min(num2_acc, num3_acc, num5_acc)

    if numbers[i] == num2_acc:
        numbers[i] = num2_acc
        i2 += 1
        num2_acc = numbers[i2] * num2

    if numbers[i] == num3_acc:
        numbers[i] = num3_acc
        i3 += 1
        num3_acc = numbers[i3] * num3

    if numbers[i] == num5_acc:
        numbers[i] = num5_acc
        i5 += 1
        num5_acc = numbers[i5] * num5

print(numbers[n - 1])

# 1 2 3 4 5 6