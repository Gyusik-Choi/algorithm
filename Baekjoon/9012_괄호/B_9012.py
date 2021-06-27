import sys


def check_valid(lst):
    stack = []
    for item in lst:
        if item == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(item)

    if len(stack) != 0:
        return False
    return True


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    ps = list(sys.stdin.readline().rstrip())
    ans = check_valid(ps)
    if ans:
        sys.stdout.write("YES" + "\n")
    else:
        sys.stdout.write("NO" + "\n")
