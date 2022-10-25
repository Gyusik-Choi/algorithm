def update(start, end, idx, target_idx, value):
    if target_idx < start or target_idx > end:
        return

    # 트리를 타고 내려 가면서
    # 범위 안에 있는 요소 갱신
    segment_tree[idx] += value

    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, idx * 2, target_idx, value)
    update(mid + 1, end, idx * 2 + 1, target_idx, value)


def consecutive_sums(start, end, idx, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return segment_tree[idx]

    mid = (start + end) // 2
    return consecutive_sums(start, mid, idx * 2, left, right) + consecutive_sums(mid + 1, end, idx * 2 + 1, left, right)


def init_segment_tree(start, end, idx):
    if start == end:
        segment_tree[idx] = arr[start]
        return segment_tree[idx]

    mid = (start + end) // 2
    segment_tree[idx] = init_segment_tree(start, mid, idx * 2) + init_segment_tree(mid + 1, end, idx * 2 + 1)
    return segment_tree[idx]


arr = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
segment_tree = [0] * (len(arr) * 4)

init_segment_tree(0, len(arr) - 1, 1)
print(segment_tree)

sums = consecutive_sums(0, len(arr) - 1, 1, 6, 8)
print(sums)

update(0, len(arr) - 1, 1, 11, 5)
print(segment_tree)

# 참고
# https://m.blog.naver.com/ndb796/221282210534

# 연속합 구할 때 left <= start and end <= right 조건이 이해가 잘 되지 않았다
# 아래의 경우가 이해 하는데 도움이 됐다
# consecutive_sums(0, len(arr) - 1, 1, 4, 8) 경우 처럼
# 4 ~ 8 구간(인덱스)의 연속합 구하는 경우에
# arr 의 4번 인덱스 값은
# start 4, end 4, left 4, right 8 에서 나오게 된다
# 여기서 보듯이 start 가 left 랑 같을 지라도 end < right 인 경우가 있을 수 있다
# 또한 반대의 경우도 나올 수 있다
# arr 6번 부터 8번 까지의 값에서 이를 볼 수 있다
# start 6, end 8, left 4, right 8 인 경우로
# end 와 right 가 같을 지라도 left <= start 하다
# arr 5번 인덱스 값은
# start 5, end 5, left 4, right 8 의 경우로
# left < start, end < right 하다
# 6번 부터 8번 까지의 값은 6, 7, 8 각각 있는 인덱스 값이 아니라
# 6 ~ 8 까지의 합을 담은 인덱스 값이다
# segment_tree 의 6번 인덱스 값이며
# 해당 인덱스 노드의 자식 노드는 각각 6 ~ 7, 8 값을 갖는다
# 이들은 조건 자체는 만족 하는데 탐색을 6 ~ 8 까지만 하게 된다
# (6 ~ 11 에서 내려온) 6 ~ 8 에서 return segment_tree[idx] 를 하기 때문에
# 자식 노드로 추가 탐색이 없게 된다
