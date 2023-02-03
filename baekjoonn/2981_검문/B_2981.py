from math import sqrt
import sys


def get_gcd(first, second):
    if second == 0:
        return first
    return get_gcd(second, first % second)


N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

subtractions = []
for i in range(1, len(numbers)):
    subtractions.append(abs(numbers[i] - numbers[i - 1]))

gcd = subtractions[0]
for j in range(1, len(subtractions)):
    gcd = get_gcd(gcd, subtractions[j])

divisor = []
for k in range(2, int(sqrt(gcd)) + 1):
    if gcd % k == 0:
        divisor.append(k)
        divisor.append(gcd // k)

divisor.append(gcd)
divisor = sorted(list(set(divisor)))
print(*divisor)
