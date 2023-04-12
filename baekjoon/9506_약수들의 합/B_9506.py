import math


while True:
    n = int(input())

    if n == -1:
        break

    square_root = int(math.sqrt(n))

    nums = [1]
    sums = 1

    for root in range(2, square_root + 1):
        quotient, remainder = divmod(n, root)

        if remainder:
            continue

        nums.append(root)
        sums += root

        if root != quotient:
            nums.append(quotient)
            sums += quotient

    nums.sort()

    if sums == n:
        divisors = ''

        for num in nums:
            divisors += str(num) + ' + '

        formatted_divisors = divisors.rstrip(' + ')
        print(f'{n} = {formatted_divisors}')
    else:
        print(f'{n} is NOT perfect.')
