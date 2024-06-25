import re


def solution(dart_result):
    result = re.findall('(\d+)([SDT])([*#]?)', dart_result)
    point = []
    for i, v in enumerate(result):
        p, b, o = v
        point.append(int(p))

        if b == 'S':
            point[i] **= 1
        elif b == 'D':
            point[i] **= 2
        else:
            point[i] **= 3

        if o == '*':
            point[i] *= 2
            if i > 0:
                point[i - 1] *= 2
        elif o == '#':
            point[i] *= -1

    return sum(point)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
