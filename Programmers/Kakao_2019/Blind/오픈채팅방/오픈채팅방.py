def solution(record):
    # record 길이가 100,000 이하로 제시되었다.
    # 시간복잡도를 줄이기 위해 이중 for 문은 피하자.
    user_dict = dict()
    for user in record:
        # split 을 통해 배열로 저장된다.
        user = user.split(" ")
        if len(user) != 2:
            # Leave 외에 split 하면 길이 3이다.
            # user[0] = 상태, user[1] = 아이디, user[2] = 닉네임
            # 가장 마지막에 나온 아이디의 닉네임이 딕셔너리의 value 로 저장된다.
            user_dict[user[1]] = user[2]

    answer = []
    for user in record:
        user = user.split(" ")
        if user[0][0] == "E":
            answer.append(user_dict[user[1]] + "님이 들어왔습니다.")
        elif user[0][0] == "L":
            answer.append(user_dict[user[1]] + "님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
