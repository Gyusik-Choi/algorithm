import sys


def downward(idx, num):
    cnt = 0
    while idx > 0:
        if numbers[idx - 1] == num:
            idx -= 1
            cnt += 1
        else:
            break
    return cnt


def upward(idx, num):
    cnt = 0
    while idx < N - 1:
        if numbers[idx + 1] == num:
            idx += 1
            cnt += 1
        else:
            break
    return cnt


def binary_search(start, end, target):
    if start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            upward_cnt = upward(mid, target)
            downward_cnt = downward(mid, target)
            return upward_cnt + downward_cnt + 1

        if numbers[mid] > target:
            return binary_search(start, mid - 1, target)
        else:
            return binary_search(mid + 1, end, target)
    else:
        return 0


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)

M = int(sys.stdin.readline().rstrip())
number_to_find = list(map(int, sys.stdin.readline().split()))

answer = []
for number in number_to_find:
    ans = binary_search(0, N - 1, number)
    answer.append(str(ans))

sys.stdout.write(' '.join(answer))
