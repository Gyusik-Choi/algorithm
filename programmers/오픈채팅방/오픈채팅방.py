from collections import defaultdict


def is_change(state):
    return state == 'Change'


def is_leave(state):
    return state == 'Leave'


def is_enter(state):
    return state == 'Enter'


def solution(record):
    # nick dict (ID: 닉네임) (ex> {uid1234: Muzi}
    # result 는 나중에 닉네임을 바꿔야 할 수 있어서
    # full 문장으로 하지 않고 id 만 갖고 있다가
    # 나중에 마지막에 for 문 돌면서 full 문장을 만든다

    nick_dict = defaultdict(str)
    result = []

    for idx, r in enumerate(record):
        record_info = r.split()

        # Leave 의 경우 Enter, Change 와 달리
        # 닉네임 정보가 없어서 split 하면 길이가 2다
        # Enter, Change 는 3이다
        if len(record_info) == 2:
            record_info.append(nick_dict[record_info[1]])

        state, user_id, nick_name = record_info
        nick_dict[user_id] = nick_name

        if is_enter(state) or is_leave(state):
            result.append([user_id, state])

    answer = []

    for r in result:
        user_id, state = r
        nick_name = nick_dict[user_id]

        if is_enter(state):
            answer.append(nick_name + "님이 들어왔습니다.")
        else:
            answer.append(nick_name + "님이 나갔습니다.")

    return answer


print(solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]))
