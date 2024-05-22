class Node:
    def __init__(self, num):
        # 기준값
        self.num = num
        # 대상 인덱스
        self.idx = 0
        # 누적합
        self.value = num


n = int(input())

two = Node(2)
three = Node(3)
five = Node(5)

dp = [1]

for i in range(1, n):
    # 최소 누적합을 갖는 객체를 구한다
    min_node = min(two, three, five, key=lambda x: x.value)
    dp.append(min_node.value)

    # dp 에 넣어준 가장 최근 값과 같은 누적합을 갖고 있는 객체의 경우
    # 대상 객체가 dp 배열에서 가장 최근에 누적합을 구하기 위해 접근한
    # 인덱스의 다음 인덱스 값과 자신의 기준값을 곱해서 누적합을 갱신한다

    if dp[i] == two.value:
        two.idx += 1
        two.value = dp[two.idx] * two.num

    if dp[i] == three.value:
        three.idx += 1
        three.value = dp[three.idx] * three.num

    if dp[i] == five.value:
        five.idx += 1
        five.value = dp[five.idx] * five.num

print(dp[n - 1])

# 참고
# https://ooyoung.tistory.com/75
# https://docs.python.org/ko/3/library/functions.html?highlight=min#min
