import sys


def get_gcd(first, second):
    pass


N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

subtractions = []
for i in range(1, len(numbers)):
    subtractions.append(abs(numbers[i] - numbers[i - 1]))

gcd = []
for j in range(1, len(subtractions)):
    g = get_gcd(subtractions[j - 1], subtractions[j])
    gcd.append(g)
