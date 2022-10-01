def get_right_length(target, idx):
    cnt = 0

    while idx < N and target == numbers[idx]:
        cnt += 1
        idx += 1

    return cnt


def get_left_length(target, idx):
    cnt = 0

    while idx >= 0 and target == numbers[idx]:
        cnt += 1
        idx -= 1

    return cnt


def get_target_length(target, idx):
    cnt = 0

    # 배열의 idx 인덱스 값이 target 과 같으면 1 더한다
    # 대상 숫자가 없는 경우는 1 더하지 않아 0
    if target == numbers[idx]:
        cnt += 1

    if idx == 0:
        cnt += get_right_length(target, idx + 1)
    else:
        if idx == N - 1:
            cnt += get_left_length(target, idx - 1)
        else:
            cnt += get_right_length(target, idx + 1)
            cnt += get_left_length(target, idx - 1)

    return cnt


def binary_search(target, start, end):
    if start >= end:
        return end

    mid = (start + end) // 2

    if numbers[mid] == target:
        return mid
    else:
        if numbers[mid] < target:
            return binary_search(target, start, mid - 1)

        return binary_search(target, mid + 1, start)


N, x = map(int, input().split())
numbers = list(map(int, input().split()))
x_idx = binary_search(x, 0, N - 1)
answer = get_target_length(x, x_idx)
if not answer:
    print(-1)
else:
    print(answer)

# 7 2
# 1 1 2 2 2 2 3

# 참고
# https://velog.io/@xxwb__/%EC%9D%B4%EA%B2%83%EC%9D%B4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%EC%A0%95%EB%A0%AC%EB%90%9C-%EB%B0%B0%EC%97%B4%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
