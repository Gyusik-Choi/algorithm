# B_14888 복사본 파일과의 차이를 잘 이해하기!
# idx 및 기타 요소들을 직접 수정해서 변수의 값 자체를 바꾸는 것과 인자의 값만 바꾸는 것의 차이
# 사용하고 해제를 해줘야 한다!

def back_track(idx, start_number, addition, subtraction, multiply, division):
    global max_num, min_num
    if idx == N - 1:
        max_num = max(start_number, max_num)
        min_num = min(start_number, min_num)
        return
    else:
        if addition:
            idx += 1
            start_number += numbers[idx]
            addition -= 1
            back_track(idx, start_number, addition, subtraction, multiply, division)
            start_number -= numbers[idx]
            idx -= 1
            addition += 1

        if subtraction:
            idx += 1
            start_number -= numbers[idx]
            subtraction -= 1
            back_track(idx, start_number, addition, subtraction, multiply, division)
            start_number += numbers[idx]
            idx -= 1
            subtraction += 1

        if multiply:
            idx += 1
            start_number *= numbers[idx]
            multiply -= 1
            back_track(idx, start_number, addition, subtraction, multiply, division)
            start_number //= numbers[idx]
            idx -= 1
            multiply += 1

        if division:
            if start_number >= 0:
                idx += 1
                start_number //= numbers[idx]
                division -= 1
                back_track(idx, start_number, addition, subtraction, multiply, division)
                start_number *= numbers[idx]
                idx -= 1
                division += 1
            else:
                idx += 1
                start_number *= -1
                start_number //= numbers[idx]
                start_number *= -1
                division -= 1
                back_track(idx, start_number, addition, subtraction, multiply, division)
                start_number *= numbers[idx]
                idx -= 1
                division += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_num = -float('inf')
min_num = float('inf')

start = numbers[0]
back_track(0, start, operators[0], operators[1], operators[2], operators[3])
print(max_num)
print(min_num)
