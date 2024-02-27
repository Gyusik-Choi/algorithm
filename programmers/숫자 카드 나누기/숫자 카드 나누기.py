# 최대 공약수
def get_gcd(first, second):
    if second == 0:
        return first
    return get_gcd(second, first % second)


# 나누어 지는지
def is_divided(arr, num):
    for a in arr:
        if not a % num:
            return True
    return False


def solution(array_a, array_b):
    a_gcd = array_a[0]

    for a in array_a[1:]:
        a_gcd = get_gcd(a_gcd, a)
        if a_gcd == 1:
            break

    b_gcd = array_b[0]

    for b in array_b[1:]:
        b_gcd = get_gcd(b_gcd, b)
        if b_gcd == 1:
            break

    answer = 0

    # gcd 가 1이면 is_divided 는 True 라서
    # 해당 if 문을 충족할 수 없다
    if not is_divided(array_a, b_gcd):
        answer = max(answer, b_gcd)

    if not is_divided(array_b, a_gcd):
        answer = max(answer, a_gcd)

    return answer


print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))

# 참고
# https://allmymight.tistory.com/198
# https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2-%EC%88%AB%EC%9E%90-%EB%82%98%EB%88%84%EA%B8%B0-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%ED%98%B8%EC%A0%9C%EB%B2%95
