# def check(p):
#     if p == '':
#         return ''
#     stack = []
#     for i in range(len(p)):
#         if p[i] == "(":
#             stack.append(p[i])
#         else:
#             if len(stack) == 0:
#                 return 0
#             elif stack[-1] == "(":
#                 stack.pop()
#
#     if len(stack) == 0:
#         return 1
#
#
# def solution(p):
#     # 처음부터 올바른 괄호 문자열인지 체크
#     num = check(p)
#     # 올바르면 그대로 끝
#     if num == 1:
#         return p
#     # 아니라면
#     else:
#         # 두 문자열 분리
#         u = []
#         v = []
#         u1 = 0
#         v1 = 0
#         for i in p:
#             if i == ")":
#                 u1 += 1
#                 u.append(i)
#             else:
#                 v1 += 1
#                 u.append(i)
#             # u가 균형잡힌 괄호 문자열 조건 만족하는지 검사(u1과 v1의 숫자가 같을 때 만족한다)
#             if u1 > 0:
#                 if u1 == v1:
#                     # u에 붙이고 남은 나머지를 v로 append 한다.
#                     v.append(p[u1 + v1:])
#                     break
#         # u가 올바른 문자열인지 체크
#         u_check = check(u)
#         # u가 올바른 문자열이면
#         if u_check == 1:
#             solution(v)
#         # 아니면
#         else:
#             empty = list()
#             empty.append("(")
#             # v에 1단계부터 재귀적으로 수행(4-2)
#             a = solution(v)
#             empty.append(a)
#             empty.append(")")
#             if len(u) > 0:
#                 u.pop(0)
#             if len(u) > 0:
#                 u.pop()
#             for i in range(len(u)):
#                 if u[i] == ")":
#                     u[i] = "("
#                 else:
#                     u[i] = ")"
#             empty.append(u)
#             return empty
#
#
# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))


# def check(p):
#     if p == '':
#         return ''
#     stack = []
#     for i in range(len(p)):
#         if p[i] == "(":
#             stack.append(p[i])
#         else:
#             if len(stack) == 0:
#                 return 0
#             elif stack[-1] == "(":
#                 stack.pop()
#
#     if len(stack) == 0:
#         return 1
#
#
# def solution(p):
#     if p == "":
#         return p
#     else:
#         # 두 문자열 분리
#         u = []
#         v = []
#         u1 = 0
#         v1 = 0
#         for i in range(len(p)):
#             # u가 균형잡힌 괄호 문자열 조건 만족하는지 검사(u1과 v1의 숫자가 같을 때 만족한다)
#             if u1 > 0:
#                 if u1 == v1:
#                     # u에 붙이고 남은 나머지를 v로 append 한다.
#                     v.append(p[u1 + v1:])
#                     break
#             else:
#                 if p[i] == ")":
#                     u1 += 1
#                     u.append(p[i])
#                 else:
#                     v1 += 1
#                     u.append(p[i])
#
#         # u가 올바른 문자열인지 체크
#         u_check = check(u)
#         # u가 올바른 문자열이면
#         if u_check == 1:
#             return u + solution(v)
#         # 아니면
#         else:
#             u_change = []
#             if u[0] == "(":
#                 u_change.append(")")
#             else:
#                 u_change.append("(")
#             if u[-1] == "(":
#                 u_change.append(")")
#             else:
#                 u_change.append("(")
#             return "(" + solution(v) + ")" + u_change

# 위에서 삽질을 해댔다. u와 v를 빈 배열로 하고 append 를 했으니 당연히 v 배열로 solution 이 재귀 돌면 solution 의 인자 배열의 길이는 당연히 1이다...
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
            return u + solution(v)
        # 아니면
        else:
            empty = ""
            empty += "("
            empty += solution(v)
            empty += ")"
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
