def solution(dart_result):
    idx = 0
    point = []
    bonus = []
    option = []

    while idx < len(dart_result):
        if dart_result[idx + 1].isdigit():
            point.append(int(dart_result[idx: idx + 2]))
            bonus.append(dart_result[idx + 2])
            if idx + 3 < len(dart_result) and dart_result[idx + 3] in ['*', '#']:
                option.append(dart_result[idx + 3])
                idx += 4
            else:
                option.append('')
                idx += 3
        else:
            point.append(int(dart_result[idx]))
            bonus.append(dart_result[idx + 1])
            if idx + 2 < len(dart_result) and dart_result[idx + 2] in ['*', '#']:
                option.append(dart_result[idx + 2])
                idx += 3
            else:
                option.append('')
                idx += 2

    for i in range(len(point)):
        b = bonus[i]
        o = option[i]

        if b == 'S':
            point[i] *= 1
        elif b == 'D':
            point[i] **= 2
        else:
            point[i] **= 3

        if o == '*':
            if i > 0:
                point[i - 1] *= 2
            point[i] *= 2
        elif o == '#':
            point[i] *= -1
        else:
            pass

    return sum(point)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
