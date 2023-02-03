import sys


def two_pointers(left, right):
    cnt = 0
    while left < right:
        sums = sequences[left] + sequences[right]
        if sums == x:
            cnt += 1
            left += 1
            right -= 1
        else:
            if sums > x:
                right -= 1
            else:
                left += 1

    return cnt


n = int(sys.stdin.readline().rstrip())
sequences = list(map(int, sys.stdin.readline().split()))
sequences.sort()
x = int(sys.stdin.readline().rstrip())

answer = two_pointers(0, n - 1)
print(answer)
