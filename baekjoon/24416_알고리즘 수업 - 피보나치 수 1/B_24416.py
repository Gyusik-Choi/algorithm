def fibo_recursion(num):
    num_info = [0] * (num + 1)
    num_info[1] = num_info[2] = 1

    for i in range(3, num + 1):
        num_info[i] = num_info[i - 1] + num_info[i - 2]
    return num_info[num]


def fibo_dynamic(num):
    return num - 2


n = int(input())
print(fibo_recursion(n), fibo_dynamic(n))

# 참고
# https://www.acmicpc.net/board/view/125928
# https://papapapa.tistory.com/27
# https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-24416-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
# 문제에 나오는 재귀 수도 코드를 그대로 구현하면 시간 초과가 발생한다
# 재귀 호출 횟수를 구하는 함수를 동적 프로그래밍 방식을 사용해서 구현한다
