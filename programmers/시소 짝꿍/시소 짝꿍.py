from collections import Counter


def solution(weights):
    cnt = 0
    counter = Counter(weights)

    for w, w_cnt in counter.items():
        # 1:1
        if w_cnt > 1:
            cnt += w_cnt * (w_cnt - 1) // 2
        # // 가 아닌 / 연산에 주의
        # 270 의 경우
        # 270 * 3 / 4 는 202.5 고
        # 270 * 3 // 4 는 202 다
        # 202 가 weights 에 존재 했다면
        # cnt 에 추가가 됐을 것이다
        #
        # 딕셔너리는 정수.0 (ex> 1.0, 27.0) 으로 접근할 경우
        # 딕셔너리에 해당 정수.0 의 키가 존재하지 않는다면
        # 암시적으로 뒤의 .0 은 제거가 되는 것 같다
        # 예를 들어
        # dic = {1: 2} 를 dic[1.0] 으로 조회하면 2가 나온다
        # dic = {1: 2, 1.0, 3} 을 dic[1.0] 으로 조회하면 3이 나온다
        #
        # 2:3
        if w * 2 / 3 in counter:
            cnt += counter[w * 2 / 3] * w_cnt
        # 2:4
        if w * 2 / 4 in counter:
            cnt += counter[w * 2 / 4] * w_cnt
        # 3:4
        if w * 3 / 4 in counter:
            cnt += counter[w * 3 / 4] * w_cnt

    return cnt


print(solution([100, 180, 360, 100, 270, 202]))

# 참고
# https://school.programmers.co.kr/questions/43248

