import sys


n = int(sys.stdin.readline().rstrip())
stack_sequence = []
number_sequence = []
sorted_numbers = [i for i in range(1, n + 1)]
numbers = []
for i in range(n):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

flag = True
j = 0
while j < len(numbers):
    num = numbers[j]
    while sorted_numbers:
        if num > sorted_numbers[0]:
            sorted_num = sorted_numbers.pop(0)
            number_sequence.append(sorted_num)
            stack_sequence.append("+")
        else:
            if num == sorted_numbers[0]:
                sorted_num = sorted_numbers.pop(0)
                stack_sequence.append("+")
                stack_sequence.append("-")
                j += 1
                break
            else:
                if num > number_sequence[-1]:
                    flag = False
                    break
                else:
                    if num < number_sequence[-1]:
                        number_sequence.pop()
                        stack_sequence.append("-")
                    else:
                        number_sequence.pop()
                        stack_sequence.append("-")
                        j += 1
                        break

    if not flag or not sorted_numbers:
        break

second_flag = True

if not flag:
    sys.stdout.write("NO" + "\n")
else:
    while j < len(numbers):
        num = numbers[j]
        if num > number_sequence[-1]:
            number_sequence.pop()
            stack_sequence.append("-")
            j += 1
        else:
            if num == number_sequence[-1]:
                number_sequence.pop()
                stack_sequence.append("-")
                j += 1
            else:
                second_flag = False
                break

    if not second_flag:
        sys.stdout.write("NO" + "\n")
    else:
        while number_sequence:
            number_sequence.pop(0)
            stack_sequence.append("-")
        for stack_seq in stack_sequence:
            sys.stdout.write(stack_seq + "\n")
