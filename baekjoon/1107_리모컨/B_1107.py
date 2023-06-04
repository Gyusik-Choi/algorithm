def get_min_move(target_channel, current_channel, perm):
    if target_channel == current_channel:
        return 0

    candidate_channel = int(''.join(list(map(str, perm))))

    # 버튼 눌러서 이동할 수 있는 채널인데
    # +, - 를 눌러서 가는게 더 빠를 수 있어서
    # 둘 중 최소값 리턴
    if candidate_channel == target_channel:
        return min(
            len(str(target_channel)),
            abs(target_channel - current_channel)
        )

    return min(
        len(str(candidate_channel)),
        abs(candidate_channel - current_channel)
    ) + abs(candidate_channel - target_channel)


def get_permutations(perms, temp, limit):
    if len(temp) == limit:
        perms.append(temp[:])
        return

    for k in range(button_length):
        # 7자리(백만) 인 경우 1의 자리가 1인 경우만 탐색
        if limit == 7 and not temp and buttons[k] != 1:
            continue

        # 10 이상의 숫자를 찾는 경우 1의 자리에 0이 오는 경우는 제외
        if limit > 1 and not temp and not buttons[k]:
            continue
        temp.append(buttons[k])
        get_permutations(perms, temp, limit)
        temp.pop()

    return perms


N = int(input())
M = int(input())
cur_channel = 100
buttons = [i for i in range(10)]
broken_buttons = []
# EOF Error 방지
if M > 0:
    broken_buttons = list(map(int, input().split()))

for i, b in enumerate(broken_buttons):
    buttons.remove(b)

button_length = len(buttons)
channel_length = len(str(N))

permutations = []

for i in range(1, 8):
    permutations.extend(get_permutations([], [], i))

min_move = abs(N - cur_channel)

for idx, permutation in enumerate(permutations):
    min_move = min(min_move, get_min_move(N, cur_channel, permutation))

print(min_move)

# 참고
# 반례
# https://www.acmicpc.net/board/view/22586
# EOF Error
# https://ahn3330.tistory.com/126
