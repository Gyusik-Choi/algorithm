numbers = [1]
num2 = 2
num3 = 3
num5 = 5

last_added_nums = [1]
while len(numbers) < 1000:
    will_add_nums = []
    for num in last_added_nums:
        will_add_nums.append(num2 * num)
        will_add_nums.append(num3 * num)
        will_add_nums.append(num5 * num)

    will_add_nums = list(set(will_add_nums))
    numbers += will_add_nums
    last_added_nums = will_add_nums

print(sorted(numbers))
