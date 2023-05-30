from collections import defaultdict


def solution(id_list, report, k):
    report = list(set(report))
    # { 신고자, [신고 당한 자] }
    report_call = defaultdict(list)
    # { 신고 당한자: 신고 당한 횟수 }
    report_dict = defaultdict(int)

    for idx, users in enumerate(report):
        a, b = users.split()
        report_call[a].append(b)
        report_dict[b] += 1

    # 신고 당한 횟수가 k 이상인 자
    target_user = []

    for idx, user in enumerate(id_list):
        if report_dict[user] >= k:
            target_user.append(user)

    # answer = [0] * len(id_list)
    #
    # for idx, user in enumerate(id_list):
    #     for value in report_call[user]:
    #         for i, target in enumerate(target_user):
    #             if target in value:
    #                 answer[idx] += 1

    # 위 주석 처리한 방식은 문제가 있다
    # id_list 를 for loop 돌면서 id_list 의 원소를
    # report_call 의 키로 접근한 값을 for loop 를 돈다
    # report_call 의 값을 for loop 돌면 나오는 원소는
    # 리스트가 아니라 리스트 안의 원소다
    # 이를 다시 target_user 를 for loop 돌면서
    # target_user 의 원소가 report_call 의 값에 포함 되는지 보는데
    # 문자열 간의 비교가 발생한다
    # 리스트에 target_user 의 원소가 있는지 확인 한다고 착각 했는데
    # 실제로는 문자열 비교를 하고 있었다
    #
    # 문자열 간의 비교로 발생할 수 있는 문제는
    # a = 'ab', b = 'abc' 라고 할때 a in b 는 참이 되는 점이다
    # 그래서 report_call[user] 에 ['ryan'] 이 있고
    # target 이 'rya' 라고 하면
    # if target in value 는 참이 된다

    answer = {i: 0 for i in id_list}

    for key, value in report_call.items():
        for idx, target in enumerate(target_user):
            if target in value:
                answer[key] += 1

    return list(answer.values())


# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
