import sys


n = int(sys.stdin.readline().rstrip())
# 정답을 담을 배열
stack_sequence = []
# 숫자를 담는 배열(스택)
number_sequence = []
# 오름차순으로 넣을 숫자
sorted_numbers = [i for i in range(1, n + 1)]
# 입력받은 숫자
numbers = []
for i in range(n):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

flag = True
j = 0
# 입력받은 숫자들을 하나씩 꺼낸다
while j < len(numbers):
    num = numbers[j]
    # 오름차순으로 넣을 숫자들을 하나씩 검사
    while sorted_numbers:
        # 입력받은 숫자가 오름차순으로 넣을 숫자보다 클 경우 아직 스택에서 빼야할 숫자가 나오지 않았다.
        # 스택에 담고 정답 배열에 +를 추가한다
        if num > sorted_numbers[0]:
            sorted_num = sorted_numbers.pop(0)
            number_sequence.append(sorted_num)
            stack_sequence.append("+")
        # 입력받은 숫자가 오름차순으로 넣을 숫자보다 작거나 같을 경우
        else:
            # 같을 경우 스택에 넣었다 빼야하므로 굳이 그 과정을 하지 않는다
            # 오름차순 숫자를 빼주고 그 다음 숫자부터 다시 검사할 수 있도록 하고
            # 정답 배열에 +와 -를 넣어준다
            # 입력받은 숫자와 일치하는 숫자를 찾았으므로
            # 입력받은 숫자도 그 다음 숫자부터 다시 검사할 수 있도록 j 를 1 올리고
            # 오름차순을 도는 while 문을 종료한다
            if num == sorted_numbers[0]:
                sorted_num = sorted_numbers.pop(0)
                stack_sequence.append("+")
                stack_sequence.append("-")
                j += 1
                break
            # 입력받은 숫자가 오름차순으로 넣을 숫자보다 작을 경우는
            # 추가적으로 스택의 숫자도 고려해야 한다
            # 오름차순 배열에서는 더 넣을 숫자가 없어서 스택에서 숫자를 뺄 수 있는지를 봐야하기 때문이다
            # 이전의 경우에는 스택에서 숫자를 빼지 않았지만 여기서 뺄 수 있는 가능성이 있다
            else:
                # 입력받은 숫자보다 스택의 숫자가 더 작으면 뺄 숫자가 나오지 않는다
                # 이미 더 작은 숫자가 스택의 최상단에 있기 때문에 스택의 안에는 더 작은 숫자들이 존재하기 때문이다
                # NO 인 경우가 되므로 while 문을 종료시키고 바깥의 while 문도 종료시킬 수 있도록 flag 변수의 값을 False 로 바꿔준다
                if num > number_sequence[-1]:
                    flag = False
                    break
                # 입력받은 숫자보다 스택의 숫자가 더 크거나 같을 경우를 나누었다
                else:
                    # 입력받은 숫자보다 스택의 숫자가 더 크면 입력받은 숫자와 스택의 숫자가 같은 수가 나올 수 있다
                    # 같은 수를 찾을 수 있도록 스택에서 숫자를 제거하고 정답 배열에는 -를 추가한다
                    if num < number_sequence[-1]:
                        number_sequence.pop()
                        stack_sequence.append("-")
                    # 입력받은 숫자와 스택의 숫자가 같으면 스택에서 수를 빼면 된다
                    # 오름차순의 숫자가 아닌 스택의 숫자이므로
                    # 스택에서 숫자를 빼고 정답 배열에 -를 추가한다
                    # 입력받은 숫자와 같은 수를 오름차순의 숫자는 아니지만 스택에서 찾았으므로
                    # 다음 입력받은 숫자를 검사할 수 있도록 j 를 1 올려주고 안쪽 while 문을 끝낸다
                    else:
                        number_sequence.pop()
                        stack_sequence.append("-")
                        j += 1
                        break
    # flag 가 False 이면 while 문을 더 돌지 않고 NO 를 출력할 수 있도록 바깥 while 문을 종료한다
    # 오름차순 숫자가 더 이상 남아있지 않으면 이제 입력받은 숫자와 스택을 비교하기 위해 바깥 while 문을 종료한다
    if not flag or not sorted_numbers:
        break

# 입력받은 숫자와 스택에서 같은 숫자를 찾을 가능성이 있는지 여부나
# 정상적으로 while 문이 끝났는지 검사하는 변수
second_flag = True

if not flag:
    sys.stdout.write("NO" + "\n")
else:
    # 위의 while 문에서 진행한 다음 입력 숫자부터 다시 검사한다
    # 오름차순 숫자는 모두 검사했고 스택에서 숫자를 빼는 일만 남았다
    # 스택에서 숫자를 뺄 수 있는지 봐야한다
    while j < len(numbers):
        num = numbers[j]
        # number_sequence 는 없는데
        # 입력받은 숫자를 다 돌지 않았으면
        # 입력받은 숫자를 처리하지 못한 것이라 아래 else 문에서 break 해서 while 문을 종료하고
        # while 문 이후에 second_flag 와 함께 j 의 값을 검사해서 NO 를 출력한다
        if number_sequence:
            # 입력받은 숫자가 스택의 숫자보다 클 경우
            # 스택에서 숫자를 빼서 입력받은 숫자와 같은 숫자를 찾을 수 있도록 한다
            if num < number_sequence[-1]:
                number_sequence.pop()
                stack_sequence.append("-")
            else:
                # 입력받은 숫자와 스택의 숫자가 같을 경우
                # 스택에서 숫자를 제거하고 정답배열에 -를 추가한다
                # j 를 1 올려서 다음 입력 숫자를 검색한다
                if num == number_sequence[-1]:
                    number_sequence.pop()
                    stack_sequence.append("-")
                    j += 1
                # 입력받은 숫자보다 스택의 숫자가 더 작으면
                # 입력받은 숫자를 스택에서 만날 수 없어지므로
                # second_flag 를 False 로 바꾸고 while 문을 종료시킨다
                else:
                    second_flag = False
                    break
        else:
            break

    if not second_flag or j < len(numbers):
        sys.stdout.write("NO" + "\n")
    else:
        for stack_seq in stack_sequence:
            sys.stdout.write(stack_seq + "\n")
