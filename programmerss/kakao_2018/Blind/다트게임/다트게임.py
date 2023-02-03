import re


def solution(dartresult):
    # \d 숫자와 매치여부를 판단하고 +를 추가하여 10처럼 두자리수로 나올 경우르 대비
    # SDT 중에서 매치여부를 판단
    # *# 중에서 매치 여부를 판단하고 ?를 추가하여 반드시 나오지 않아도 되게끔 처리
    answer = []
    pattern = re.compile('(\d+)([SDT])([*#]?)')
    points = pattern.findall(dartresult)

    for point in points:
        # S일 경우
        if point[1] == "S":
            answer.append(int(point[0]))
            # *일 경우
            if point[2] == "*":
                answer[-1] *= 2
                # 첫번째에 *가 나온게 아닐 경우
                if len(answer) >= 2:
                    answer[-2] *= 2
            # #일 경우
            elif point[2] == "#":
                answer[-1] *= -1

        # D일 경우
        elif point[1] == "D":
            answer.append(int(point[0]) ** 2)
            if point[2] == "*":
                answer[-1] *= 2
                if len(answer) >= 2:
                    answer[-2] *= 2
            elif point[2] == "#":
                answer[-1] *= -1

        # T일 경우
        else:
            answer.append(int(point[0]) ** 3)
            if point[2] == "*":
                answer[-1] *= 2
                if len(answer) >= 2:
                    answer[-2] *= 2
            elif point[2] == "#":
                answer[-1] *= -1

    return sum(answer)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
