operation = input()

numbers = []
operations = []
# 숫자만 모으는 변수
temp = ''
for o in operation:
    if o != '-' and o != '+':
        # 연산자가 아니면 숫자니까 temp 변수에 더해준다
        temp += o
    else:
        # 연산자가 나오면 temp 변수 값을 배열에 넣고
        temp = int(temp)
        numbers.append(temp)
        # 연산자도 배열에 넣는다
        operations.append(o)
        # 변수를 빈 문자열로 처리
        temp = ''
# 마지막 남은 숫자 처리
numbers.append(int(temp))

for i in range(len(operations) - 1):
    if operations[i] == '-':
        idx = i
        flag = False
        while idx < len(operations) - 1:
            if operations[idx + 1] == '+':
                flag = True
                numbers[idx + 2] = numbers[idx + 1] + numbers[idx + 2]
                numbers[idx + 1] = 0
                idx += 1
            else:
                break
        if flag:
            numbers[i + 1] = numbers[idx + 1]
            numbers[idx + 1] = 0

for i in range(len(operations)):
    if operations[i] == '-':
        numbers[i + 1] = numbers[i] - numbers[i + 1]
        numbers[i] = 0
    else:
        numbers[i + 1] = numbers[i] + numbers[i + 1]
        numbers[i] = 0

print(numbers[-1])
