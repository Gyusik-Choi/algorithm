def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # for 문을 한번 돌면서 두 배열 요소간의 논리 연산 후 이진수로 변환 -> 정수에서 문자열
        logical = format(arr1[i] | arr2[i], 'b')
        # 1과 0을 각각 #과 공백으로 변환
        # 여기서 딕셔너리로 변환되고 translate 메소드를 통해 비로소 원하는 형태가 된다.
        change_to_dict = logical.maketrans('10', '# ')
        dict_to_str = logical.translate(change_to_dict)
        # n보다 변환한 문자열의 길이가 짧다면 짧은 수만큼 앞에 0을 붙인다.
        if n - len(dict_to_str) != 0:
            for i in range(n - len(dict_to_str)):
                dict_to_str = ' ' + dict_to_str
            answer.append(dict_to_str)
        else:
            answer.append(dict_to_str)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
