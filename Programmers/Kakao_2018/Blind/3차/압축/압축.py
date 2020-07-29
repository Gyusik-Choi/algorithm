def solution(msg):
    answer = []
    # alphabet 딕셔너리에 아스키코드 값을 활용하여 A ~ Z 까지 1 ~ 26을 value 로 각각 넣어준다.
    alphabet = dict()
    for num in range(ord('A'), ord('Z') + 1):
        alphabet[chr(num)] = num - 64
    # 딕셔너리에 없는 단어가 나올 때 까지 반복문을 돌며 word 에 더해준다.
    # 딕셔너리에 없는 단어가 나오면 그 앞까지는 존재했다는 것이므로
    # 마지막 단어를 제외한 딕셔너리의 word 값을 slice 하여 answer 에 넣는다.
    # 그리고 딕셔너리에는 word 값을 key 로 하고, 기존 alphabet 의 value 최대값에서 1을 더한 값을 value 로 하여 추가한다.
    i = 0
    while i < len(msg):
        word = ''
        for j in range(i, len(msg)):
            word += msg[j]
            # j == len(msg) - 1은 마지막 인덱스를 처리하기 위한 조건
            if word not in alphabet or j == len(msg) - 1:
                # 마지막 인덱스를 두 조건으로 나누어 판단
                if j == len(msg) - 1:
                    # 마지막 인덱스까지 구해진 word 가 alphabet 에 없다면 새로운 단어가 아직 있다는 것이므로 answer 에 마지막 단어를 제외한 딕셔너리의 word 값을 넣어주고
                    # i에 j 값을 넣어주어 연산을 더 수행한다.
                    if word not in alphabet:
                        answer.append(alphabet[word[:-1]])
                        alphabet[word] = max(alphabet.values()) + 1
                        i = j
                        break
                    # 마지막 인덱스까지 구해진 word 가 alphabet 에 있다면 새로운 단어가 더 이상 없다는 뜻이므로 answer 에 딕셔너리의 word 값을 넣어주고 끝낸다.
                    else:
                        answer.append(alphabet[word])
                        i = len(msg)
                        break
                # 마지막 인덱스까지 오지 않았고 지금까지 구한 word 가 딕셔너리에 없는 경우
                else:
                    answer.append(alphabet[word[:-1]])
                    alphabet[word] = max(alphabet.values()) + 1
                    i = j
                    break
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
