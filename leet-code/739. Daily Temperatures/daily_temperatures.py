def daily_temperatures(temperatures: list[int]):
    stack = []
    answer = [0] * len(temperatures)

    for cur, t in enumerate(temperatures):
        # stack 에 값이 아닌 인덱스를 넣어서
        # stack 에서 꺼냈을 때
        # temperatures 의 어떤 값에 해당 하는지
        # 정확하게 찾을 수 있다
        # 만약에 stack 에 값을 넣었다면
        # temperatures 에 중복된 값이 있을 경우
        # 중복된 값 중에서 어떤 값인지 판단하기 까다롭다
        while stack and t > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = cur - prev
        stack.append(cur)

    return answer


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(daily_temperatures([30, 40, 50, 60]))
print(daily_temperatures([30, 60, 90]))
