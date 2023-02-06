numbers = list(map(int, input()))

answer = 0
for number in numbers:
    if answer > 1 and number > 1:
        answer *= number
    else:
        answer += number

print(answer)

# 참고
# https://velog.io/@xxwb__/이것이-코딩-테스트다-그리디-곱하기-혹은-더하기
