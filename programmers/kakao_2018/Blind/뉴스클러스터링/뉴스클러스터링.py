def solution(str1, str2):
    # 모두 대문자로 변환
    a = str1.upper()
    b = str2.upper()

    # 배열화
    c = list()
    d = list()

    # 두개씩 입력값이 모두 대문자면 append
    for i in range(len(a) - 1):
        if "A" <= a[i] <= "Z" and "A" <= a[i + 1] <= "Z":
            c.append(a[i] + a[i + 1])
    for i in range(len(b) - 1):
        if "A" <= b[i] <= "Z" and "A" <= b[i + 1] <= "Z":
            d.append(b[i] + b[i + 1])

    # 각 요소들의 key 값을 넣고 갯수를 세어준다
    c_dict = dict()
    for i in c:
        if i in c_dict:
            c_dict[i] += 1
        else:
            c_dict[i] = 1
    d_dict = dict()
    for i in d:
        if i in d_dict:
            d_dict[i] += 1
        else:
            d_dict[i] = 1

    inter = dict()
    uni = dict()

    # 교집합 계산
    for k1, v1 in c_dict.items():
        if k1 not in d_dict:
            continue
        else:
            for k2, v2 in d_dict.items():
                if k1 == k2:
                    if v1 > d_dict[k2]:
                        inter[k1] = v2
                    else:
                        inter[k1] = v1

    # A의 합집합 계산
    for k1, v1 in c_dict.items():
        if k1 not in uni:
            uni[k1] = v1
        else:
            if uni[k1] > v1:
                continue
            else:
                uni[k1] = v1
    # B의 합집합 계산
    for k2, v2 in d_dict.items():
        if k2 not in uni:
            uni[k2] = v2
        else:
            if uni[k2] > v2:
                continue
            else:
                uni[k2] = v2

    if len(inter) == 0 and len(uni) == 0:
        return 65536
    else:
        answer = int(sum(inter.values()) / sum(uni.values()) * 65536)
        return answer


print(solution("FRANCE", "french"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
