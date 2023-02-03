# 올바른 괄호 문자열인지 확인하는 함수
def check(p):
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        else:
            if len(stack) == 0:
                return 0
            elif stack[-1] == "(":
                stack.pop()

    if len(stack) == 0:
        return 1


def solution(p):
    if p == "":
        return p
    else:
        # 두 문자열 분리
        u = ""
        v = ""
        u1 = 0
        v1 = 0
        for i in p:
            # u가 균형잡힌 괄호 문자열 조건 만족하는지 검사(u1과 v1의 숫자가 같을 때 만족한다)
            if u1 > 0 and u1 == v1:
                # u에 붙이고 남은 나머지를 v로 append 한다.
                v += p[u1 + v1:]
                break
            else:
                if i == ")":
                    u1 += 1
                    u += i
                else:
                    v1 += 1
                    u += i

        # u가 올바른 문자열인지 체크
        u_check = check(u)

        # u가 올바른 문자열이면
        if u_check == 1:
            ans = solution(v)
            return u + ans

        # 아니면
        else:
            empty = ""
            empty += "("
            empty += solution(v)
            empty += ")"
            # u의 처음과 끝부분 제거
            u = u[1:-1]
            for i in u:
                if i == ")":
                    empty += "("
                else:
                    empty += ")"
            return empty


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
