def solution(babbling):
    cnt = 0
    pronounce_list = ["aya", "ye", "woo", "ma"]

    for babble in babbling:
        is_possible = False
        prev = ''
        cur = ''

        for i, b in enumerate(babble):
            cur += b

            if cur not in pronounce_list:
                continue

            # 직전 비교와 동일
            # 발음 X
            if prev == cur:
                is_possible = False
                break

            # 마지막 인덱스
            # 발음 O
            if i == len(babble) - 1:
                is_possible = True
                break

            # 아직 끝까지 검사 안한 상태
            # bab 까지는 발음 O
            # 직전 비교 발음 값을 bab 로 갱신
            # bab 을 초기화 시켜서 나머지 babble 요소 검사할 수 있도록 한다
            prev = cur
            cur = ''

        if is_possible:
            cnt += 1

    return cnt


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
