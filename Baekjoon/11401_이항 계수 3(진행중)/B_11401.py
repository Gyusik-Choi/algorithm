N, K = map(int, input().split())

# 이 문제를 풀기 위해 필요한 수학 개념들
# 항
# 이항계수
# 모듈러 연산
# 역원, 항등원
# 페르마의 소정리
# 음의 지수

# 이항계수는 조합 공식으로 풀 수 있다
# n! // (k! * (n - k)!)
# n! // k! // (n - k)!
# 그런데 모듈러 연산에는 나눗셈 연산이 없다
# 역원(역수)을 활용해야 한다
# 역원은 항등원을 만드는 숫자다(덧셈의 항등원은 0, 곱셈의 항등원은 1)
# 주의할점은 분모 부분인 k! * (n - k)! 의 역원을 구한다는 점이다

# 일반 곱셈의 역원이라면 a는 a ^ -1 이 된다 (a * a ^ -1 = 1 이므로)
# 모듈러 연산의 역원은 조금 다르다
# 모듈러 연산에서 a의 역원은 a * b mod c = 1
# a랑 곱해서 c로 나눈 나머지가 1을 만족하는 숫자다
# 모듈러 연산에서 a의 역원은 페르마의 소정리를 통해 쉽게 구할 수 있다

# 문제에서의 입력을 기준으로 하면
# N이 정수, K가 소수이면서
# N이 K의 배수가 아니라면
# N ^ K mod X = N mod X
# N ^ K - 1 mod X = 1 mod X
# 여기까지는 이해가 잘 됐는데
# N mod X의 역원이 N ^ K - 2 mod X 라는 점이 잘 이해가 안 됐다

# 개념들이 확실하게 정리가 되지 못했다
# 어려운 내용들이 많아서 공부가 좀 더 필요하다

# https://st-lab.tistory.com/241
# https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses
