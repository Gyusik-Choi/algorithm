def length_of_longest_substring(s: str) -> int:
    used = dict()
    start = 0
    max_length = 0

    for idx, char in enumerate(s):
        # char 가 used 에 이미 있으면서
        # start <= used[char] 인 경우
        # 앞서 char 가 이미 나왔던 위치에서
        # 한 칸 뒤를 새로운 start 로 설정한다
        #
        # start > used[char] 인 경우는
        # char 가 used 에 있기는 하지만
        # 이미 앞서 char 가 나왔던 위치보다
        # start 가 더 뒤에 있어서
        # 앞서 char 가 나온 위치는
        # 범위를 벗어났다
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, idx - start + 1)
        # used[char] 는 현재 인덱스로 매번 갱신한다
        used[char] = idx

    return max_length


print(length_of_longest_substring("abcabcbb"))

# 아래는 start > used[char] 인 경우가 포함된 입력
# 마지막 d 가 start > used[char] 인 경우다
# 마지막 d 가 나왔을때 start 는 4인데
# used[char] 는 0이다 (d 가 이전에 0번째 인덱스에서 나왔다)
#
# 마지막 d 가 나왔을때
# 이미 start 는 4가 돼서
# longest_substring 을 판단하는 시작 위치는 4가 됐다
# used[char] 는 0이라
# longest_substring 의 시작 위치 보다 앞에 있다
# 마지막 d 는 else 문에서 max_length 를 계산하는 범위에 포함된다
print(length_of_longest_substring("dabcabcd"))

# 위의 입력과 달리 d 가 마지막에 2개 연속으로 나온다
# 여기서 마지막 2개 중 첫번째 d 는
# 위의 입력과 같이 start > used[char] 라
# else 문으로 빠진다
# 마지막 2개 중 두번째 d 는
# 앞선 d 에 의해서 used[char] 가 갱신된다
# start <= used[char] 를 만족해서
# if 문으로 빠진다
print(length_of_longest_substring("dabcabcdd"))