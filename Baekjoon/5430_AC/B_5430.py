from collections import deque
import sys


def remove_number(d):
    if not d:
        deq.popleft()
    else:
        deq.pop()


def length_check():
    if not len(deq):
        return False
    return True


def change_direction(d):
    if not d:
        d = 1
    else:
        d = 0
    return d


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    numbers = sys.stdin.readline().rstrip()[1: -1].split(',')

    deq = deque()
    if numbers[0] != '':
        deq += list(map(int, numbers))
    else:
        deq += numbers

    # 0 = left, 1 = right
    direction = 0
    # error 여부
    flag = True

    if deq[0] == "":
        if "D" in p:
            flag = False
    else:
        for i in range(len(p)):
            func = p[i]
            if func == "R":
                direction = change_direction(direction)
            else:
                if not length_check():
                    flag = False
                    break
                else:
                    remove_number(direction)

    if flag:
        answer = '['
        if not len(deq):
            answer += "]"
        elif deq[0] == "":
            answer += "]"
        else:
            if not direction:
                for j in range(len(deq) - 1):
                    answer += str(deq[j]) + ","
                answer += str(deq[-1]) + "]"
            else:
                for j in range(len(deq) - 1, 0, -1):
                    answer += str(deq[j]) + ","
                answer += str(deq[0]) + "]"
        sys.stdout.write(answer + "\n")
    else:
        sys.stdout.write("error" + "\n")

# 제출하니 IndexError
# 반례
# https://www.acmicpc.net/board/view/73842
