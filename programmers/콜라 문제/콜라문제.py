# 마트가 주는 콜라 병 수
def find_new_coke(multiple, a, b):
    return multiple // a * b

# 마트에 주어야 하는 병 수
def find_max_multiple(a, n):
    # 방법 1
    # multiple = a
    # while True:
    #     # if a + a <= n:
    #     #     a += a
    #     # 처음에 위처럼 했으나
    #     # a 가 누적 되므로 안 된다
    #
    #     if multiple + a <= n:
    #         multiple += a
    #     else:
    #         break
    # return multiple

    # 방법 2
    return n // a * a


def solution(a, b, n):
    answer = 0
    # n 보다 작거나 같은 a 의 배수
    # 새 콜라 받아서 마시면 빈 콜라가 되므로
    # 받은 콜라는 무조건 마신 것으로 생각
    total_coke = n

    while total_coke >= a:
        multiple = find_max_multiple(a, total_coke)
        new_coke = find_new_coke(multiple, a, b)

        # 남은 콜라 병 수에서 마트에 주어야 하는 병 수를 빼고
        total_coke -= multiple
        # 남은 콜라 병 수에서 마트가 준 병 수 더한다
        total_coke += new_coke

        # 마트가 준 병 수 더한다
        answer += new_coke

    return answer


print(solution(2, 1, 20))
print(solution(3, 1, 20))
