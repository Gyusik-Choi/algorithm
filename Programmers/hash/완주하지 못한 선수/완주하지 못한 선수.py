# 오답코드
# def solution(participant, completion):
#     answer = ''
#     for i in participant:
#         if i not in completion:
#             answer = i
#             break
#     if len(answer) == 0:
#         result = {}
#         for k in participant:
#             result[k] = participant.count(k)
#         for j in result:
#             if result[j] > 1:
#                 answer = j
#     return answer


# 정확성은 통과하나 효율성에서 실패
# def solution(participant, completion):
#     comp = {}
#     for i in completion:
#         comp[i] = completion.count(i)
#     for i in participant:
#         if i not in comp:
#             return i
#         else:
#             comp[i] -= 1
#             if com[i] < 0:
#                 return i


# 정답코드
# 코딩도장에 소개된 fromkeys 활용
def solution(participant, completion):
    comp = dict.fromkeys(completion, 0)
    for i in completion:
        comp[i] += 1
    for i in participant:
        comp[i] -= 1
        if i not in comp or comp[i] < 0:
            return i


participant = ["leo", "kiki", "eden", "leo"]
completion = ["eden", "kiki", "leo"]
print(solution(participant, completion))
