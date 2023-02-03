def get_gcd(first, second):
    if second == 0:
        return first
    return get_gcd(second, first % second)


N = int(input())
numbers = list(map(int, input().split()))
status = numbers[0]
for i in range(1, len(numbers)):
    gcd = get_gcd(status, numbers[i])
    print("{}/{}".format(status // gcd, numbers[i] // gcd))
