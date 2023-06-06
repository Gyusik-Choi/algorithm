def get_min_move(target_channel, current_channel, perm):
    # 이동하려는 채널이 100인 경우
    if target_channel == current_channel:
        return 0

    # 순열로 찾은 후보 채널
    candidate_channel = int(''.join(list(map(str, perm))))

    # 이동하려는 채널이 +, - 버튼 없이
    # 숫자 버튼만 눌러서 이동 가능한 경우
    #
    # 그런데
    # +, - 를 눌러서 가는게 더 빠를 수 있어서
    # 둘 중 최소값 리턴
    if candidate_channel == target_channel:
        return min(
            # 숫자 버튼 누르는 횟수
            len(str(target_channel)),
            # + 혹은 - 를 누르는 횟수
            # target_channel 이 current_channel 보다
            # 클 수도 작을 수도 있어서 절대값 구한다
            abs(target_channel - current_channel)
        )

    # 이동하려는 채널이
    # 숫자 버튼만 눌러서 이동할 수 없는 경우
    # 숫자 버튼과 +, - 버튼을 함께 쓰거나 혹은
    # +, - 버튼만 눌러서 이동해야 한다
    return min(
        len(str(candidate_channel)),
        abs(candidate_channel - current_channel)
    # 이 경우는 현재 채널에서 이동하려는 채널 (target_channel) 로
    # 바로 갈 수 없어서
    # 현재 채널에서 candidate_channel 를 거쳐서
    # 이동하려는 채널로 가야 한다
    # candidate_channel 에서 target_channel 은
    # 숫자 버튼이 아닌 +, - 로만 이동이 가능해서
    # candidate_channel 에서 target_channel 를 뺀 절대값 구한다
    ) + abs(candidate_channel - target_channel)


def get_permutations(perms, temp, limit):
    if len(temp) == limit:
        perms.append(temp[:])
        return

    for k in range(button_length):
        # 10 이상의 숫자를 찾는 경우
        # 1의 자리에 0이 오는 경우 제외
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
min_move = abs(N - cur_channel)

# 500000 이 최대 채널이라
# 최대 탐색 범위를
# 999999 로 제한한다
# 만약에
# 목표 채널이 500000 이면
# 1000000 에서 - 버튼 눌러서 이동하는 것보다
# 현재 위치인 100 에서 + 버튼 눌러서 이동하는게
# 더 빠르다
for i in range(1, 7):
    permutations.extend(get_permutations([], [], i))

for idx, permutation in enumerate(permutations):
    min_move = min(min_move, get_min_move(N, cur_channel, permutation))

print(min_move)

# 참고
# 반례
# https://www.acmicpc.net/board/view/22586
# EOF Error
# https://ahn3330.tistory.com/126
